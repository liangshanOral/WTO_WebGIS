var myFlowChart = echarts.init(document.getElementById('flow'));
var pieChart1 = echarts.init(document.getElementById('pie1'));
var pieChart2 = echarts.init(document.getElementById('pie2'));
var organization = document.getElementById('organization');

var names = [];


var data = {};
// 页面加载时初始化 Select2
document.addEventListener('DOMContentLoaded', function () {
    // 初始化国家和产品的 Select2
    $('#datatype').select2({
        width: '100%',
        placeholder: 'Search or select...',
        allowClear: true,
        multiple: false
    });
    $('#time').select2({
        width: '100%',
        placeholder: 'Search or select...',
        allowClear: true,
        multiple: false
    });

    fillSelect2('time', [2020, 2019, 2018, 2017, 2016, 2015]);
    fillSelect2('datatype', ['Export', 'Import'])
    // 获取国家和产品数据
    // fetch('/get-flow-data/')
    //     .then(response => response.json())
    //     .then(data => {
    //         fillSelect2('datatype', data.products);
    //     })
    //     .catch(error => {
    //         console.error('Error fetching country and product data:', error);
    //     });
});

//不知道为什么不能从其他js中import
function initSelect2(elementId) {
    // 使用 Select2 初始化选择列表
    $('#' + elementId).select2({
        width: '100%',
        placeholder: 'Search or select...',
        allowClear: true,
        multiple: false,
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
    switch (organization.value) {
        case 'G20':
            names = ['China', 'Argentina', 'Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'Japan', 'Korea, Republic of', 'Mexico', 'Russian Federation', 'Saudi Arabia, Kingdom of', 'South Africa', 'Türkiye', 'United Kingdom', 'United States of America', 'European Union'];
            break;
        case 'APEC':
            names = ['China', 'Hong Kong, China', 'Chinese Taipei', 'Australia', 'Brunei Darussalam', 'Canada', 'Chile', 'Indonesia', 'Japan', 'Korea, Republic of', 'Malaysia', 'Mexico', 'New Zealand', 'Peru', 'Papua New Guinea', 'Philippines', 'Russian Federation', 'Singapore', 'Thailand', 'United States of America', 'Vietnam'];
            break;
        case 'BRICS':
            names = ['Brazil', 'Russian Federation', 'India', 'China', 'South Africa'];
            break;
        case 'FVEY':
            names = ['United States of America', 'United Kingdom', 'Canada', 'Australia', 'New Zealand'];
            break;
        case 'CRExpress':
            names = ['China', 'Kazakhstan', 'Russia', 'Belarus', 'Poland', 'Germany', 'Netherlands', 'Belgium', 'France', 'Spain', 'Italy', 'Austria', 'Hungary', 'Serbia', 'Bulgaria', 'Turkey', 'Georgia', 'Azerbaijan', 'Caspian Sea', 'Turkmenistan', 'Uzbekistan', 'Kyrgyzstan', 'Tajikistan', 'Afghanistan', 'Iran', 'Iraq'];
            break;
    }
    // 获取用户选择的国家和产品
    const selectedTime = $('#time').val();
    const selectedType = $('#datatype').val();

    // 发送请求到后端获取数据
    if (selectedType == 'Export') {
        data = fetch(`/echarts-flow-data-export/?time=${selectedTime}`)
            .then(response => response.json())
            .then(data => {
                // 处理后端返回的数据，更新 ECharts 图表
                console.log('Data from the backend:', data);
                updateflow(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    } else if (selectedType == 'Import') {
        data = fetch(`/echarts-flow-data-import/?time=${selectedTime}`)
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

    backendData = data;
    //console.log(backendData.nodes);

    // 构建节点数据
    var nodesData = backendData.nodes.map(function (node) {
        if (names.includes(node[0])) {
            return {
                name: node[0],
                value: [node[2], node[1]]
            };
        }
    }).filter(node => node);
    //console.log(nodesData)
    // 构建边数据
    const minVal = -10000;
    const maxVal = 30000;
    var edgesData = backendData.edges.map(function (edge) {
        var opacity = (edge.value - minVal) / (maxVal - minVal);
        var color = `rgba(255, 0, 0, ${opacity})`;
        // 使用 Math.min() 来确保线宽不超过最大值
        var lineWidth = 10;

        return {
            source: edge.source,
            target: edge.target,
            value: edge.value,
            lineStyle: { lineWidth: lineWidth, color: color }
        };
    });
    //console.log(edgesData)
    // 构建箭头的样式
    var arrowStyle = {
        normal: {
            width: 0.5,
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
            center: [0, 0], // 调整地图的中心坐标
            zoom: 1 // 调整地图的缩放级别
        },
        series: [{
            type: 'graph',
            coordinateSystem: 'geo',
            layout: 'force',
            symbolSize: 5, // 设置节点大小
            roam: true,
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [4, 10],
            data: nodesData,
            links: edgesData,
            lineStyle: arrowStyle,
            emphasis: {
                focus: 'adjacency',
                lineStyle: {
                    width: 2
                }
            },
            force: {
                repulsion: 10
            }
        }],
        tooltip: {
            show: true,
            formatter: function (params) {
                if (params.dataType === 'edge') {
                    return 'Value: ' + params.data.value;
                }
                return '';  // 如果不是边，则返回空字符串，即不显示 tooltip
            }
        }
    };
    // 假设你已经有了 myChart 对象，并且 nodesData 和 edgesData 包含了节点和边的数据
    myFlowChart.on('click', function (params) {
        if (params.dataType === 'node') {
            // 当点击节点时
            var clickedNode = params.data;
            var relatedEdges = findRelatedEdges(clickedNode, edgesData);
            var relatedNodes = findRelatedNodes(clickedNode, relatedEdges);
            var importEdges = findImportEdges(clickedNode, edgesData);
            var exportEdges = findExportEdges(clickedNode, edgesData);

            // 更新图表显示，只显示相关的节点和边
            updateChartWithNodesAndEdges(relatedNodes, relatedEdges);
            generatepiechartWithImportEdges(clickedNode, importEdges);
            generatepiechartWithExportEdges(clickedNode, exportEdges);
        } else {
            myFlowChart.setOption({
                series: [{
                    data: nodesData,
                    links: edgesData

                }
                ]
            })
        }
    });

    // 找到与节点相关的边
    function findRelatedEdges(node, allEdges) {
        var relatedEdges = [];
        for (var i = 0; i < allEdges.length; i++) {
            var edge = allEdges[i];
            if (edge.source === node.name || edge.target === node.name) {
                relatedEdges.push(edge);
            }
        }
        return relatedEdges;
    }
    function findImportEdges(node, allEdges) {
        var importEdges = [];
        for (var i = 0; i < allEdges.length; i++) {
            var edge = allEdges[i];
            if (edge.target === node.name) {
                var importedge = {};
                importedge.name = edge.source;
                importedge.value = edge.value;
                importEdges.push(importedge);
            }
        }
        var result = reclass(importEdges);
        return result;
    }
    function findExportEdges(node, allEdges) {
        var exportEdges = [];
        for (var i = 0; i < allEdges.length; i++) {
            var edge = allEdges[i];
            if (edge.source === node.name) {
                var exportedge = {};
                exportedge.name = edge.target;
                exportedge.value = edge.value;
                exportEdges.push(exportedge);
            }
        }

        var result = reclass(exportEdges)

        return result;
    }
    function reclass(exportEdges) {
        var sum_export = 0;
        for (var i = 0; i < exportEdges.length; i++) {
            sum_export += Number(exportEdges[i]['value']);
        }

        console.log(sum_export);

        var result = [];
        var others = {
            name: 'others',
            value: 0,
        }
        for (var i = 0; i < exportEdges.length; i++) {
            if (Number(exportEdges[i]['value']) > 0.0005 * exportEdges.length * sum_export) {
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
    // 找到与节点相关的节点
    function findRelatedNodes(node, relatedEdges) {
        var relatedNodes = [node.name];
        for (var i = 0; i < relatedEdges.length; i++) {
            var edge = relatedEdges[i];
            if (edge.source !== node.name) {
                relatedNodes.push(edge.source);
            }
            if (edge.target !== node.name) {
                relatedNodes.push(edge.target);
            }
        }
        return relatedNodes;
    }

    // 更新图表显示，只显示相关的节点和边
    function updateChartWithNodesAndEdges(relatedNodes, relatedEdges) {
        // 更新图表的 series[0].data 和 series[0].links 属性，将其设置为相关的节点和边
        myFlowChart.setOption({
            series: [{
                data: nodesData.filter(node => relatedNodes.includes(node.name)),
                links: relatedEdges
            }]
        });
    }
    function generatepiechartWithImportEdges(clickedNode, importEdges) {
        //根据所选节点生成饼图

        var optionpie = {
            title: {
                text: clickedNode.name + ' import'
            },
            series: [
                {
                    type: 'pie',
                    radius: '55%',
                    data: importEdges
                }
            ],
            tooltip: {
                show: true,

            }
        }
        pieChart1.setOption(optionpie);
    }
    function generatepiechartWithExportEdges(clickedNode, exportEdges) {
        var optionpie = {
            title: {
                text: clickedNode.name + ' export'
            },
            series: [
                {
                    type: 'pie',
                    radius: '55%',
                    data: exportEdges
                }
            ],
            tooltip: {
                show: true,

            }
        }
        pieChart2.setOption(optionpie);
    }

    // 渲染图表
    myFlowChart.setOption(option);

}
