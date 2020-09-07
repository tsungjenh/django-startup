#### - User Login
**URI**: /api/user/login/<br />
**METHOD**: post<br />
**PARAMS**:

| name | type | required | description |
| -------- | -------- |-------- | -------- |
| name | str | Y |  user name|
| password | str | Y | password|

**RESPONSE**:
```javascript
{
    "status": 0,
    "msg": "OK",
    "timestamp": "2020-02-05 17:58:13",
    "data": {}
}
```

#### - User Logout
**URI**: /api/user/logout/<br />
**METHOD**: post<br />

**RESPONSE**:
```javascript
{
    "status": 0,
    "msg": "OK",
    "timestamp": "2020-02-05 17:58:13",
    "data": {}
}
```

#### - Register 
**URI**: /api/user/register/<br />
**METHOD**: post<br />
**PARAMS**:

| name | type | required | description |
| -------- | -------- |-------- | -------- |
| name | str | Y | user name |
| password | str | Y | password |

**RESPONSE**:
```javascript
{
    "status": 0,
    "msg": "OK",
    "timestamp": "2020-02-05 17:58:13",
    "data": {
        "id": 1,
        "created_at": "2019-11-29 17:57:09",
        "updated_at": "2019-11-29 17:57:09",
        "name": "user-01",
    }
}
```
