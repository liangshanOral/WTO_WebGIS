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

/* useless
function updateflow(response){

    // 定义节点和边的数组
    var nodes = response.nodes;
    var edges = response.edges;
    
    console.log('Nodes:', nodes);
    console.log('Edges:', edges);
    // 检查 'source' 或 'target' 是 None 或空值的情况
    // 检查 'source' 或 'target' 是 undefined、null 或空字符串的情况
    for (let i = 0; i < edges.length; i++) {
        const edge = edges[i];
        if (!edge.source || !edge.target || edge.source.trim() === '' || edge.target.trim() === '') {
            console.error(`Error: 'source' or 'target' is undefined, null, or empty in edge ${i}:`, edge);
        }
    }

    // 过滤出坐标已知的节点
    var knownNodes = nodes.filter(node => typeof node.latitude !== 0 && typeof node.longitude !== 0);

    // 过滤出只连接坐标已知节点的边
    var validEdges = edges.filter(edge => {
        // 检查边的起点和终点是否均为坐标已知的节点
        return knownNodes.find(node => node.name === edge.source) && knownNodes.find(node => node.name === edge.target);
    });

    console.log('knownnodes:', knownNodes);
    console.log('vaildedges:', validEdges);

    var cy = cytoscape({
        container: document.getElementById('flow'),
        elements: {
        nodes: knownNodes,
        edges: validEdges
        },
        style: [
          {
            selector: 'node',
            style: {
              'label': 'data(id)'
            }
          },
          {
            selector: 'edge',
            style: {
              'label': 'data(value)',
              'curve-style': 'bezier',
              'target-arrow-shape': 'triangle'
            }
          }
        ]
      });
    // 输出节点和边的信息
    console.log('Nodes:', cy.nodes().json());
    console.log('Edges:', cy.edges().json());

}*/

// 在 updateECharts 函数中处理数据并绘制流向图
function updateflow(data) {
    myChart.clear();

    // 定义节点和边的数组
    var nodes = data.nodes;
    var edges = data.edges;

    // 使用数据绘制流向图
    var option = {
        geo: {
            map: 'world',
            roam: true,
            zoom: 1.2,
            label: {
                emphasis: {
                    show: false
                }
            },
            itemStyle: {
                emphasis: {
                    areaColor: '#2a333d'
                }
            }
        },
        series: [{
            type: 'lines',
            coordinateSystem: 'geo',
            data: edges.map(edge => ({
                fromName: edge.source,
                toName: edge.target,
                coords: [ { name: edge.source, latitude: nodes[edge.source].latitude, longitude: nodes[edge.source].longitude },
                { name: edge.target, latitude: nodes[edge.target].latitude, longitude: nodes[edge.target].longitude }],
                value: edge.value
            })),
            symbolSize: 5,
            lineStyle: {
                normal: {
                    color: 'source',   // 线条颜色设为起始国家的颜色
                    width: 1,
                    opacity: 0.5,
                    curveness: 0.1
                }
            },
            emphasis: {
                lineStyle: {
                    color: '#ff7f50',
                    width: 2,
                    opacity: 1
                }
            }
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}
