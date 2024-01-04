var myChart = echarts.init(document.getElementById('main'));

// 页面加载时初始化 Select2
document.addEventListener('DOMContentLoaded', function () {
    // 初始化国家和产品的 Select2
    initSelect2('country');
    initSelect2('product');

    // 获取国家和产品数据
    fetch('/get-country-product-data/')
        .then(response => response.json())
        .then(data => {
            fillSelect2('country', data.countries);
            fillSelect2('product', data.products);
        })
        .catch(error => {
            console.error('Error fetching country and product data:', error);
        });
});

export function initSelect2(elementId) {
    // 使用 Select2 初始化选择列表
    $('#' + elementId).select2({
        width: '100%',
        placeholder: 'Search or select...',
        allowClear: true,
        multiple: true,
    });
}

export function fillSelect2(elementId, options) {
    // 清空 Select2 中的选项
    $('#' + elementId).empty();

    // 将新的选项填充到 Select2 中
    options.forEach(option => {
        $('#' + elementId).append(new Option(option, option, false, false));
    });

    // 触发 Select2 的 change 事件，使其重新渲染
    $('#' + elementId).trigger('change');
}

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

    // 使用 Set 确保国家的唯一性
    var uniqueCountriesSet = new Set(data.map(item => item.country));
    // 获取唯一国家的数量
    var uniqueCountriesCount = uniqueCountriesSet.size;

    // 根据国家数量判断情况
    if (uniqueCountriesCount > 1) {
        console.log('多国家多指标情况');
        // 遍历数据，处理多国家多指标的情况
        var groupedData = {};  // 用于多国家多指标情况的数据分组
        data.forEach(item => {
            var countryKey = item.country;  // 按国家分组
            if (!groupedData[countryKey]) {
                groupedData[countryKey] = {};
            }
            // 将每个指标的值加总到对应国家和年份
            if (!groupedData[countryKey][item.year]) {
                groupedData[countryKey][item.year] = 0;
            }
            groupedData[countryKey][item.year] += parseFloat(item.export_value_y);
            // 将国家添加到图例中，确保不重复
            if (option.legend.data.indexOf(item.country) === -1) {
                option.legend.data.push(item.country);
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
                    data: Object.values(groupedData[key])  // 使用 Object.values 转为数组
                };
                option.series.push(seriesItem);
            }
        }

    } else if (uniqueCountriesCount === 1) {
        console.log('单国家多指标情况');
        
        var groupedData = {};  
        data.forEach(item => {
            var legendName = item.product;  // 按指标分组
            if (!groupedData[legendName]) {
                groupedData[legendName] = [];
            }
            groupedData[legendName].push(parseFloat(item.export_value_y));
            // 将指标添加到图例中，确保不重复
            if (option.legend.data.indexOf(legendName) === -1) {
                option.legend.data.push(legendName);
            }
        });

        // 处理单国家多指标的数据，添加到系列中
        for (var key in groupedData) {
            if (groupedData.hasOwnProperty(key)) {
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
                    data: groupedData[key]
                };
                option.series.push(seriesItem);
            }
        }
    } else {
        console.log('没有数据或其他情况');
        // 其他情况的处理
    }
    // 使用 option 更新 ECharts 图表
    option && myChart.setOption(option);
}


