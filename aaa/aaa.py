from pushgateway_client import client

result = client.push_data(
    url="150.158.237.22:39091",         # 连接地址：此处只需要填写Pushgateway的IP地址+端口就行了，不用写http协议头，暂时只支持http连接
    metric_name="my_metric_name",       # 指标名称：此处指的就是Prometheus中的指标名（至于如何让Pushgateway中的指标投送到Prometheus中，请参阅官方文档）
    metric_value="123",                 # 指标的值：受官网当前版本的限制，目前只支持数字做为值
    job_name="demo",                    # Job名字：Prometheus会为所有的指标都追加一个job标签，在Prometheus这个job只是一个标签，但是在Pushgateway中这个job就是一个唯一标识符
    labels={                            # 标签可以自己随意设定，支持多标签；需要注意的是：<instance>标签如果不明确的指定的话，本模块会自动获取<您的主机名>来成为<instance>标签的值
        "aaa": "111",
        "bbb": "222",
        "ccc": "333",
    })

print(result)
print(type(result))
