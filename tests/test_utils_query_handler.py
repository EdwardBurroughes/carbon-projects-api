import pytest
from fastapi import HTTPException
from pytest_mock import MockerFixture

from api.utils import query_handler


class ConnectionStubb:
    def close(self):
        print("closing connection")


@pytest.mark.parametrize(
    "params, expected_params", ((None, []), (("synthetic-id",), ("synthetic-id",)))
)
def test_execute_query__executes_with_expected_params(
    mocker: MockerFixture, params, expected_params
):
    conn = ConnectionStubb()
    mocked_cursor_execute = mocker.patch.object(query_handler, "_cursor_execute")
    query_handler.execute_query(conn, "SELECT * FROM projects WHERE id=?", params)
    mocked_cursor_execute.assert_called_once_with(
        conn, "SELECT * FROM projects WHERE id=?", expected_params
    )


def test_execute_query__raises_500_error_w_bad_query(mocker: MockerFixture):
    conn = ConnectionStubb()
    mocker.patch.object(query_handler, "_cursor_execute", side_effect=ValueError)
    with pytest.raises(HTTPException) as exc_info:
        query_handler.execute_query(conn, "SELECT * FROM bad")
        assert exc_info.value.status_code == 500
