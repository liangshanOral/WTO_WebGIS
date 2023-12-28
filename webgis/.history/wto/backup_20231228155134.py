from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from .models import Country, ProductSector, TradeYearData_E

def echarts_data(request):
    # 在这里处理前端传递的参数，查询数据库，获取相应的数据
    # 示例：假设你的模型是 TradeYearData_E
    selected_country = request.GET.get('country', '')
    selected_product = request.GET.get('product', '')
    print(selected_country,selected_product)

   # 处理产品参数，分割成列表
    # 处理产品参数，确保每个产品名称被单引号包裹
    #selected_country = [f'{country.strip()}' for country in selected_country[0].split(',')]
    #selected_product = [f'{product.strip()}' for product in selected_product[0].split(',')]
    print(selected_country,selected_product)
    #queryset = TradeYearData_E.objects.filter(reporting_country__name=selected_country, product_sector__name=selected_product)
    # 查询每个国家下选择的品类的加总数据
    queryset = TradeYearData_E.objects.filter(
        reporting_country__name=selected_country,
        product_sector__name=selected_product
    ).values('year', 'export_value_y')
    #print(str(queryset.query))
    data = list(queryset)
    return JsonResponse({'data': data})

'''
function getData() {
            // 获取用户选择的国家和产品
            const selectedCountry = $('#country').val();
            const selectedProduct = $('#product').val();

            const countryParam = selectedCountry.join(',');
            const productParam = selectedProduct.join(',');

            // 发送请求到后端获取数据
            fetch(`/echarts-data/?country=${countryParam}&product=${productParam}`)
                .then(response => response.json())
                .then(data => {
                    // 处理后端返回的数据，更新 ECharts 图表
                    console.log('Data from the backend:', data); 
                    updateECharts(data);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        }

        function updateECharts(response) {
            // 从 response 中获取数据
            var data = response.data;
            // console.log("getdata:",data);
            // 提取年份和出口值
            var years = data.map(item => item.year);
            var exportValues = data.map(item => parseFloat(item.export_value_y));

            // 配置 ECharts 图表
            var option = {
                title: {
                text: 'Export Values Over Years'
                },
                tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                    backgroundColor: '#6a7985'
                    }
                }
                },
                legend: {
                data: ['Export Values']
                },
                xAxis: {
                type: 'category',
                boundaryGap: false,
                data: years
                },
                yAxis: {
                type: 'value'
                },
                series: [
                {
                    name: 'Export Values',
                    type: 'line',
                    stack: 'total',
                    label: {
                    show: true
                    },
                    emphasis: {
                    focus: 'series'
                    },
                    data: exportValues
                }
                ]
            };

            option && myChart.setOption(option);
        }

         function updateECharts(response) {

            // 清空图表
            myChart.clear();
            // 从 response 中获取数据
            var data = response.data;

            // 使用 Set 确保年份的唯一性
            var uniqueYearsSet = new Set(data.map(item => item.year));

            // 将 Set 转为数组
            var years = Array.from(uniqueYearsSet);

            // 配置 ECharts 图表
            var option = {
                title: {
                    text: 'Export Values Over Years'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        label: {
                            backgroundColor: '#6a7985'
                        }
                    }
                },
                legend: {
                    data: []  // 在这里设置图例，每个指标一个图例项
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: years
                },
                yAxis: {
                    type: 'value'
                },
                series: []  // 在这里设置系列，每个指标一个系列项
            };

            // 遍历数据，处理单国家多指标和多国家多指标的情况
            var groupedData = {};  // 用于多国家多指标情况的数据分组
            data.forEach(item => {
                var legendName = item.country + ' - ' + item.product;  // 按国家和指标分组
                if (!groupedData[legendName]) {
                    groupedData[legendName] = [];
                }
                groupedData[legendName].push(parseFloat(item.export_value_y));

                // 将指标添加到图例中，确保不重复
                if (option.legend.data.indexOf(item.product) === -1) {
                    option.legend.data.push(item.product);
                }
            });

            // 处理多国家多指标的数据，添加到系列中
            for (var key in groupedData) {
                if (groupedData.hasOwnProperty(key)) {
                    var seriesItem = {
                        name: key,
                        type: 'line',
                        stack: 'total',
                        label: {
                            show: true
                        },
                        emphasis: {
                            focus: 'series'
                        },
                        data: groupedData[key]
                    };
                    option.series.push(seriesItem);
                }
            }

            // 使用 option 更新 ECharts 图表
            option && myChart.setOption(option);
        }

        // 遍历数据，处理单国家多指标和多国家多指标的情况
        var groupedData = {};  // 用于多国家多指标情况的数据分组
        data.forEach(item => {
            var legendName = item.country + ' - ' + item.product;  // 按国家和指标分组
            if (!groupedData[legendName]) {
                groupedData[legendName] = [];
            }
            groupedData[legendName].push(parseFloat(item.export_value_y));

            // 将指标添加到图例中，确保不重复
            if (option.legend.data.indexOf(legendName) === -1) {
                option.legend.data.push(legendName);
            }
        });

        // 处理多国家多指标的数据，添加到系列中
        for (var key in groupedData) {
            if (groupedData.hasOwnProperty(key)) {
                var seriesItem = {
                    name: key,
                    type: 'line',
                    stack: 'total',
                    label: {
                        show: true
                    },
                    emphasis: {
                        focus: 'series'
                    },
                    data: groupedData[key]
                };
                option.series.push(seriesItem);
            }
        }
'''