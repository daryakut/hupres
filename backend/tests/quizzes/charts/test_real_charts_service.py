import json

import pytest

from quizzes.charts import get_chart_info, Gender, export_chart_info


@pytest.mark.asyncio
@pytest.mark.skip(reason="calling external service")
async def test_real_charts_client():
    info = get_chart_info(
        product_id=11,
        soma_type=[-2, 10, 26, 5, 1],
        respondent_name='Иван',
        gender=Gender.MALE,
    )

    # dumping the response
    print(json.dumps(export_chart_info(info)))
