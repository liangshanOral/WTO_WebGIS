var line1 = echarts.init(document.getElementById('line1'));
var line2 = echarts.init(document.getElementById('line2'));
var data = {};
function getData(countryname) {
    var selectedProduct = $('#product1').val();
    const productParam = selectedProduct.join(',');
    const countryParam = $('#country').val();
    var Time = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022];

    fetch(`/echarts-data-import/?country=${countryParam}&product=${productParam}`)
        .then(response => response.json()).then(data => {
            console.log(data);
            updateimportchart(data, Time);
        }).catch(error => {
            console.error('Error fetching data:', error);
            alert("未收录该国家的数据！");
        });
    fetch(`/echarts-data/?country=${countryParam}&product=${productParam}`)
        .then(response => response.json()).then(data => {
            console.log(data);
            updateexportchart(data, Time);
        }).catch(error => {
            console.error('Error fetching data:', error);
        });
}
function updateimportchart(response, Time) {
    line1.clear();
    var data = response.data;

    var option = {
        title: {
            text: 'Import Values (million)'
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
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: Time
        },
        legend: {
            data: []  // 在这里设置图例，每个指标一个图例项
        },
        yAxis: {
            type: 'value'
        },
        series: []  // 在这里设置系列，每个指标一个系列项
    };
    var groupedData = {};
    data.forEach(item => {
        var legendName = item.product;  // 按指标分组
        if (!groupedData[legendName]) {
            groupedData[legendName] = [];
        }
        groupedData[legendName].push({'value':parseFloat(item.import_value_y),'year':item.year});
        // 将指标添加到图例中，确保不重复
        if (option.legend.data.indexOf(legendName) === -1) {
            option.legend.data.push(legendName);
        }
    });

    // 处理单国家多指标的数据，添加到系列中
    for (var key in groupedData) {
        if (groupedData.hasOwnProperty(key)) {
            result=sortby(groupedData[key],Time);
            var seriesItem = {
                name: key,
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: result.map(element=>{
                    return element.value;
                })
            };
            option.series.push(seriesItem);
        }
    }

    line1.setOption(option);
}
function updateexportchart(response, Time) {
    line2.clear();
    var data = response.data;
    
    var option = {
        title: {
            text: 'Export Values (million) '
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
            data: Time
        },
        yAxis: {
            type: 'value'
        },
        series: []
        // 在这里设置系列，每个指标一个系列项
    };
    var groupedData = {};
    data.forEach(item => {
        var legendName = item.product;  // 按指标分组
        if (!groupedData[legendName]) {
            groupedData[legendName] = [];
        }
        groupedData[legendName].push({'value':parseFloat(item.export_value_y),'year':item.year});
        // 将指标添加到图例中，确保不重复
        if (option.legend.data.indexOf(legendName) === -1) {
            option.legend.data.push(legendName);
        }
    });

    // 处理单国家多指标的数据，添加到系列中
    for (var key in groupedData) {
        if (groupedData.hasOwnProperty(key)) {
            result=sortby(groupedData[key],Time);
            var seriesItem = {
                name: key,
                type: 'line',
                stack: 'Total',
                areaStyle: {},
                label: {
                    show: true
                },
                emphasis: {
                    focus: 'series'
                },
                data: result.map(element=>{
                    return element.value;
                })
            };
            option.series.push(seriesItem);
        }
    }

    line2.setOption(option);
}
function sortby(data, Time) {
    var result = [];
    var timely = data.map(element => {
        return element.year;
    })
    Time.forEach(element => {
        var num = timely.findIndex(year => year == element);
        if (num != -1) {
            result.push(data[num]);
        }
    });
    return result;
}