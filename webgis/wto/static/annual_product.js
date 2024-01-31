var pie1 = echarts.init(document.getElementById('pie1'));
var pie2 = echarts.init(document.getElementById('pie2'));


function getData3() {
    // 获取用户选择的国家和产品
    const selectedProduct = $('#product').val();
    const selectedTime = $('#time').val();


    // 发送请求到后端获取数据
    fetch(`/annual-product-import/?product=${selectedProduct}&time=${selectedTime}`)
        .then(response => response.json())
        .then(data => {
            // 处理后端返回的数据，更新 ECharts 图表
            console.log('Data from the backend:', data);
            updateimportcharts(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
    fetch(`/annual-product-export/?product=${selectedProduct}&time=${selectedTime}`)
        .then(response => response.json())
        .then(data => {
            // 处理后端返回的数据，更新 ECharts 图表
            console.log('Data from the backend:', data);
            updateexportcharts(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function updateimportcharts(response) {
    // 清空图表
    pie1.clear();

    // 从 response 中获取数据
    var data = response.data;
    data.sort(sortArr('value'));
    data = reclass(data);
    // 配置 ECharts 图表
    var option = {
        title: {
            text: 'Most Import Countries '
        },
        tooltip: {
            show: true,
        },
        series: [
            {
                type: 'pie',
                radius: '55%',
                data: data,
            }
        ]  // 在这里设置系列，每个指标一个系列项
    };
    // 使用 option 更新 ECharts 图表
    pie1.setOption(option);
}
function updateexportcharts(response) {
    // 清空图表
    pie2.clear();

    // 从 response 中获取数据
    var data = response.data;
    data.sort(sortArr('value'));
    data = reclass(data);
    // 配置 ECharts 图表
    var option = {
        title: {
            text: 'Most Export Countries '
        },
        tooltip: {
            show: true,
        },
        series: [
            {
                type: 'pie',
                radius: '55%',
                data: data,
            }
        ]  // 在这里设置系列，每个指标一个系列项
    };
    // 使用 option 更新 ECharts 图表
    pie2.setOption(option);
}

function sortArr(attr) {
    return function (a, b) {
        return b[attr] - a[attr]
    }
}
function reclass(exportEdges) {
    var sum_export = 0;
    for (var i = 0; i < exportEdges.length; i++) {
        sum_export += Number(exportEdges[i]['value']);
    }


    var result = [];
    var others = {
        name: 'others',
        value: 0,
    }
    for (var i = 0; i < exportEdges.length; i++) {
        if (Number(exportEdges[i]['value']) > 0.0001 * exportEdges.length * sum_export) {
            result.push(exportEdges[i]);
        } else {
            others['value'] += Number(exportEdges[i]['value']);
        }
    }
    if (Number(others['value']) == 0) {
        return result;
    }
    result.push(others);
    return result;

}

