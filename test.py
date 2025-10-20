import requests
import xml.etree.ElementTree as ET
import json

url = "https://pda.weather.gov.hk/locspc/data/fnd_e.xml"
response = requests.get(url)
xml_data = response.text

try:
    # 尝试XML解析（若仍需保留）
    root = ET.fromstring(xml_data)
    print("XML解析成功，数据节点：", root.tag)
    # 此处可添加XML提取逻辑（如不需要可注释）
except ET.ParseError:
    # XML解析失败，尝试JSON解析
    try:
        json_data = response.json()
        print("JSON解析成功，数据结构：", list(json_data.keys()))

        # 修正：forecast_detail 是列表，直接遍历
        forecast_list = json_data.get("forecast_detail", [])
        for forecast in forecast_list:
            date = forecast.get("forecast_date")
            weather_desc = forecast.get("wx_desc")
            max_temp = forecast.get("max_rh")
            min_temp = forecast.get("min_rh")
            print(f"日期：{date}，天气：{weather_desc}，最高温：{max_temp}℃，最低温：{min_temp}℃")
    except json.JSONDecodeError:
        print("XML和JSON解析均失败，数据内容异常：", xml_data[:100])