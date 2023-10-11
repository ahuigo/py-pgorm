# Pgorm
Pgorm is a simple orm for postgre in python

## install

    pip install py-pgorm==0.0.8

## Usage

    import pgorm 
    def getCursor():
        dbconf={
            "database":"<dbname>",
            "user":"<user>", 
            "password": "<password>"
        }
        cursor = pgorm.getDbCursor(dbconf)
        return cursor

    def test_create_table():
    
        cursor = getCursor()
        sql = '''
            drop table t;
            create table if not exists t(
                code varchar(10) not null, 
                label real not null
            );'''

        try:
            cursor.execute(sql) 
        except Exception as e:
            pass
    

## Examples
Refer to [examples](https://github.com/ahuigo/py-pgorm/blob/master/tests)
