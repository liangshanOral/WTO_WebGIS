var myChart = echarts.init(document.getElementById('flow'));

// 页面加载时初始化 Select2
document.addEventListener('DOMContentLoaded', function () {
    // 初始化国家和产品的 Select2
    initSelect2('product2');
    initSelect2('time');

    // 获取国家和产品数据
    fetch('/get-flow-data/')
        .then(response => response.json())
        .then(data => {
            fillSelect2('', data.countries);
            fillSelect2('product', data.products);
        })
        .catch(error => {
            console.error('Error fetching country and product data:', error);
        });
});

function initSelect2(elementId) {
    // 使用 Select2 初始化选择列表
    $('#' + elementId).select2({
        width: '100%',
        placeholder: 'Search or select...',
        allowClear: true,
        multiple: true,
    });
}