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

    backendData=data;
    //console.log(backendData.nodes);

    // 构建节点数据
    var nodesData = backendData.nodes.map(function (node) {
        return {
            name: node[0], // 假设节点数据的第一个元素是名称
            value: [node[2], node[1]] // 假设节点数据的第二个和第三个元素分别是纬度和经度
        };
    });

    // 构建边数据
    var edgesData = backendData.edges.map(function (edge) {
        return {
            source: edge[0], // 假设边数据的第一个元素是源节点名称
            target: edge[1], // 假设边数据的第二个元素是目标节点名称
            value: edge[2] // 假设边数据的第三个元素是边的权重或其他信息
        };
    });

    // 构建箭头的样式
    var arrowStyle = {
        normal: {
            width: 2,
            opacity: 1,
            curveness: 0.2, // 控制曲率，可根据需要调整
            color: 'rgb(200, 0, 0)', // 箭头颜色
            label: {
                show: true,
                position: 'middle', // 标签位置，可根据需要调整
                formatter: '{b}', // 标签内容，显示边的 value
                fontSize: 10 // 标签字体大小，可根据需要调整
            }
        }
    };

    // 设置 ECharts 配置
    var option = {
        geo: {
            map: 'world', // 使用 world 地图
            roam: true,
            center: [0, 30], // 调整地图的中心坐标
            zoom: 1 // 调整地图的缩放级别
        },
        series: [{
            type: 'graph',
            layout: 'force',
            symbolSize: 10, // 设置节点大小
            roam: true,
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [4, 10],
            edgeLabel: {
                fontSize: 10
            },
            data: nodesData,
            links: edgesData,
            lineStyle: arrowStyle,
            emphasis: {
                focus: 'adjacency',
                lineStyle: {
                    width: 10
                }
            },
            force: {
                repulsion: 100
            }
        }]
    };

    // 渲染图表
    myChart.setOption(option);
}
