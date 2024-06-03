from enum import Enum


class QueryResultType(Enum):
    SQL_QUERY_RUN_RESULT = "SQL_QUERY_RUN_RESULT"
    SQL_QUERY_STRING_RESULT = "SQL_QUERY_STRING_RESULT"
    SELECTED_TABLES = "SELECTED_TABLES"
    CHART_GENERATION_RESULT = "CHART_GENERATION_RESULT"


class QueryStreamingEventType(str, Enum):
    QUERY_OUT = "QUERY_OUT_EVENT"
    ADD_RESULT = "ADD_RESULT_EVENT"
