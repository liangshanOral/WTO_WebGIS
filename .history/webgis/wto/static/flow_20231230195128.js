var myChart = echarts.init(document.getElementById('flow'));

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
