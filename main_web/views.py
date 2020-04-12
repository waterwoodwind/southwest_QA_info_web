from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from main_web.models import qa_info
from django.core import serializers
import json
import pandas as pd
import arrow

def df_chinese_data():
    exclude_list = []

    query_data = qa_info.objects.all().order_by('-data')
    json_data = serializers.serialize("json", query_data, use_natural_foreign_keys=True)
    list_data = json.loads(json_data)

    dict_name_verbose_name = {}
    columns_set = []
    colheaders = []
    dataSchema = {}
    for field in qa_info._meta.fields:
        dict_name_verbose_name[field.name] = field.verbose_name

        if not field.verbose_name in exclude_list:
            print (field.verbose_name)
            colheaders.append(field.verbose_name.encode("utf8"))
            dataSchema[field.verbose_name] = ''
            columns_item = {
                u"title": field.verbose_name,
                u"field": field.verbose_name,
                # u"sortable": u"true",
            }
            if field.verbose_name == u"问题描述":
                columns_item[u"width"] = u"20%"
                columns_item[u"title"] = u"问题描述"
            elif field.verbose_name == u"整改措施":
                columns_item[u"width"] = u"20%"
                columns_item[u"title"] = u"整改措施"
            elif field.verbose_name == u"处理意见":
                columns_item[u"width"] = u"6%"
                columns_item[u"title"] = u"处理意见"
            else:
                split_list = list(field.verbose_name)
                # every two word add
                title_str = ""
                for i in range(len(split_list)):
                    title_str = title_str + split_list[i]
                    if (i + 1) % 2 == 0:
                        title_str = title_str + u"<br>"
                if field.verbose_name == u"相关附件":
                    columns_item[u'formatter'] = "attachment"
                columns_item[u"title"] = title_str
                columns_item[u"width"] = u"2%"
            columns_set.append(columns_item)

    json_columns = json.dumps(columns_set)

    upload_data = []
    for item in list_data:
        single_data = item['fields']
        single_data[u'id'] = item['pk']
        upload_data.append(single_data)
        # print upload_data

    chinese_updata = []
    for item in upload_data:
        dict_updata = {}
        for key, value in item.items():
            dict_updata[dict_name_verbose_name[key]] = value

            # print chinese_updata
        chinese_updata.append(dict_updata)
    return chinese_updata

def index(request):
    upload_data = json.dumps(df_chinese_data())
    return render(request, 'background.html', {'json_data': upload_data})

def month_count_group_by_department(request):
    df_data = pd.DataFrame(df_chinese_data())
    df_da = pd.DataFrame(df_chinese_data(), index=df_data[u'日期'])
    string_index = df_data[u'日期']
    # 计算出起止月份
    start_day = string_index.min()
    end_day = string_index.max()
    start_ar = arrow.get(start_day)
    end_ar = arrow.get(end_day)
    print (end_ar)

    if start_ar.day >= 26:
        number_month = start_ar.month + 1
    else:
        number_month = start_ar.month
    start_month = start_ar.replace(month=number_month)
    if end_ar.day >= 26:
        number_month = end_ar.month + 1
    else:
        number_month = end_ar.month + 1
    end_month = end_ar.shift(months=number_month)
    print (end_month)

    list_month = []
    list_month_count_scheduled = []
    list_month_count_airline1 = []
    list_month_count_airline2 = []
    list_month_count_airline3 = []

    for r in arrow.Arrow.range('month', start_month, end_month):
        year_month = r.format("YYYY-MM")
        end = arrow.get(r)
        end = end.replace(day=25)
        start = end.shift(months=-1)
        start = start.replace(day=26)
        list_a_month = []
        for r in arrow.Arrow.range('day', start, end):
            a_day = r.format('YYYY-MM-DD')
            list_a_month.append(a_day)
        try:
            df_month = df_da.loc[list_a_month]
            list_month.append(year_month)
            list_month_count_scheduled.append(int(df_month[u'受检部门/大队'][df_month[u'受检部门/大队'] == u"成都航线一大队"].count()))
            list_month_count_airline1.append(int(df_month[u'受检部门/大队'][df_month[u'受检部门/大队'] == u"成都航线二大队"].count()))
            list_month_count_airline2.append(int(df_month[u'受检部门/大队'][df_month[u'受检部门/大队'] == u"重庆分公司"].count()))
            list_month_count_airline3.append(int(df_month[u'受检部门/大队'][df_month[u'受检部门/大队'] == u"贵阳分公司"].count()))
        except:
            continue

    json_month = json.dumps(list_month)
    json_count_scheduled = json.dumps(list_month_count_scheduled)
    json_count_airline1 = json.dumps(list_month_count_airline1)
    json_count_airline2 = json.dumps(list_month_count_airline2)
    json_count_airline3 = json.dumps(list_month_count_airline3)
    return render(request, "month_count_group_by_department.html", {"json_month": json_month,
                                                                    "json_count_scheduled": json_count_scheduled,
                                                                    "json_count_airline1": json_count_airline1,
                                                                    "json_count_airline2": json_count_airline2,
                                                                    "json_count_airline3": json_count_airline3})
