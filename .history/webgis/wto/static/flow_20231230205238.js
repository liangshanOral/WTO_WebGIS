var myChart = echarts.init(document.getElementById('flow'));

// 页面加载时初始化 Select2
document.addEventListener('DOMContentLoaded', function () {
    // 初始化国家和产品的 Select2
    initSelect2('product2');
    initSelect2('time');
    
    fillSelect2('time', [2020, 2019, 2018, 2017, 2016, 2015]);

    // 获取国家和产品数据
    fetch('/get-flow-data/')
        .then(response => response.json())
        .then(data => {
            fillSelect2('product2', data.products);
        })
        .catch(error => {
            console.error('Error fetching country and product data:', error);
        });
});

//不知道为什么不能从其他js中import
function initSelect2(elementId) {
    // 使用 Select2 初始化选择列表
    $('#' + elementId).select2({
        width: '100%',
        placeholder: 'Search or select...',
        allowClear: true,
        multiple: true,
    });
}

function fillSelect2(elementId, options) {
    // 清空 Select2 中的选项
    $('#' + elementId).empty();

    // 将新的选项填充到 Select2 中
    options.forEach(option => {
        $('#' + elementId).append(new Option(option, option, false, false));
    });

    // 触发 Select2 的 change 事件，使其重新渲染
    $('#' + elementId).trigger('change');
}

function getData2() {
    // 获取用户选择的国家和产品
    const selectedTime = $('#time').val();
    const selectedProduct = $('#product2').val();

    const TimeParam = selectedTime.join(',');
    const productParam = selectedProduct.join(',');

    // 发送请求到后端获取数据
    fetch(`/echarts-flow-data/?time=${TimeParam}&product=${productParam}`)
        .then(response => response.json())
        .then(data => {
            // 处理后端返回的数据，更新 ECharts 图表
            console.log('Data from the backend:', data); 
            updateflow(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function updateflow(response){
    myChart.clear();

    var dataForFrontend = response;
    console.log(response);
    // 定义节点和边的数组
    var nodes = dataForFrontend.nodes;
    var edges = dataForFrontend.edges;

    // 使用数据绘制流向图
    var option = {
        series: [{
            type: 'graph',
            layout: 'force',
            data: nodes,
            links: edges,
            force: {
                repulsion: 100,
                edgeLength: 30,
            },
            coordinateSystem: 'geo', // 设置坐标系为地理坐标系
            roam: true, // 开启漫游
            label: {
                show: true, // 显示标签
                position: 'right', // 标签位置
            },
            emphasis: {
                focus: 'adjacency', // 高亮相邻节点和边
            },
            edgeSymbol: ['circle', 'arrow'], // 边的起始和终止符号
            edgeSymbolSize: [4, 10], // 边的起始和终止符号的大小
        }],
    };

    myChart.setOption(option);
    
}