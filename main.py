import pytest
import json
from common.request_method import RequestMethod
from common.do_data import DoData
from common.log import Log

test_data = DoData.do_excel("./data/data.xlsx", "API")
log = Log()

ids = [i for i in range(1, len(test_data)+1)]


@pytest.mark.parametrize("id,url,method,data,expect_result", test_data, ids=ids)
def test_case(id, url, method, data, expect_result):
    log.info(f"编号:{id},请求url:{url},方法:{method},数据:{data},期望结果:{expect_result}")
    data = json.loads(data)
    res = RequestMethod.do_request(url, method, data)
    res_json = res.json()
    try:
        assert res_json == json.loads(expect_result)
        log.info(f"编号:{id}运行通过")
    except AssertionError:
        log.info(f"编号:{id}运行失败", exc_info=True)
        raise AssertionError

# res = requests.post(url, data=test_data)
# print(res.json())
