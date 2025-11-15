from __future__ import annotations


from peewee import SqliteDatabase
from utils import (app, PreloadJs, dataclass,
                   field, ClassVar, CREATE_META_TABLE,
                   GET_META_VERSION, SET_META_VERSION)


@dataclass
class Db(PreloadJs):
    """
    Class for handling database operations.
    """
    path: str = field(default=app.config.get_param("data", "json_path"))
    schema_version: int = field(default=app.config.get_param("data", "schema_version"))
    db: SqliteDatabase = field(init=False)
    _META_SQL: ClassVar[str] = CREATE_META_TABLE
    path_db: str = field(default=PreloadJs.BASE_DIR / app.config.get_param("data", "db_path"))

    def __post_init__(self) -> None:
        super().__post_init__()
        self.db = self._get_db() or None
    def _get_db(self) -> SqliteDatabase:
        """
        Get the database object.
        """
        return SqliteDatabase(str(self.path_db), pragmas=self.data, timeout=5)

    # --- low-level meta helpers ---
    def _ensure_meta(self):
        self.db.execute_sql(self._META_SQL)

    def _get_version(self) -> int | None:
        cur = self.db.execute_sql(GET_META_VERSION)
        row = cur.fetchone()
        return int(row[0]) if row else None

    def _set_version(self, v: int):
        self.db.execute_sql(SET_META_VERSION, (str(v),))

        # --- public API ---

    def create_or_migrate(self) -> int:
        """
        Create or migrate a database.
        :return: The current schema version.
        """
        self.db.connect(reuse_if_open=True)
        from models.models_orm import db_proxy, TagModel, TaskTagModel, TaskModel
        db_proxy.initialize(self.db)
        with self.db.atomic():
            self._ensure_meta()
            ver = self._get_version()
            if ver is None:
                # fresh install
                self.db.create_tables([TagModel, TaskModel, TaskTagModel])
                self._set_version(self.schema_version)
                return self.schema_version

            while ver < self.schema_version:
                self._migrate_step(ver, ver + 1)
                ver += 1
                self._set_version(ver)
            return ver

    def _migrate_step(self, frm: int, to: int):
        # пример:
        # if frm == 1 and to == 2:
        #     migrator = SqliteMigrator(self.db)
        #     migrate(migrator.add_column('task', 'due', DateTimeField(null=True)))
        pass


db = Db()
