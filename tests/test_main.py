from pgorm import getDbCursor, insertBatch, insertUpdate
dbconf={
    "database":"ahuigo",
    "user":"ahui", 
}
cursor = getDbCursor(dbconf)

# test alter column
def test_alter_column():
    cursor.execute(f'alter table t DROP CONSTRAINT  IF EXISTS code_pkey')
    sql = f'alter table t add CONSTRAINT code_pkey UNIQUE (code);'
    cursor.execute(sql)

# test insert batch
def test_insert_batch():
    # row = {"op": "0001", "action": "profit", "time": datetime.today()}
    # import pandas as pd
    # rows = pd.DataFrame([{'code':'00000.XX',"label":3}])
    rows = [
        {"code": "a", "label": 2},
        {"code": "code4", "label": 4},
    ]
    insertBatch(cursor, 't', rows, onConflictKeys="code")

# test insert update
def test_insert_update():
    row = {"code": "a", "label": 3}
    insertUpdate(cursor, "t", row, onConflictKeys="code")

    # count
    cursor.execute(f'select count(*) as count from t ')
    row = cursor.fetchone()
    assert row[0]>=2

# test fetchone
def test_fetchone():
    # fetchone 
    cursor.execute(f'select code,label from t where code=%s limit 1', ['a'])
    assert cursor.query==b"select code,label from t where code='a' limit 1"
    res = cursor.fetchone()
    assert res["label"] == 3
    assert res[1] ==3

    # fetch none
    cursor.execute(f'select code,label from t where code=%s limit 1', ['not exists'])
    assert cursor.fetchone()==None

