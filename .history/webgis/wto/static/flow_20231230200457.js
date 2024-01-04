// 使用相对路径引入 file1.js
import { fillSelect2, initSelect2 } from './graph.js';

var myChart = echarts.init(document.getElementById('flow'));

// 页面加载时初始化 Select2
document.addEventListener('DOMContentLoaded', function () {
    // 初始化国家和产品的 Select2
    initSelect2('product2');
    initSelect2('time');
    // 然后就可以在这里使用 fillSelect2 和 initSelect2 函数了
    fillSelect2('time', [2021, 2020, 2019, 2018, 2017, 2016, 2015]);

    // 获取国家和产品数据
    fetch('/get-flow-data/')
        .then(response => response.json())
        .then(data => {
            fillSelect2('product', data.products);
        })
        .catch(error => {
            console.error('Error fetching country and product data:', error);
        });
});

