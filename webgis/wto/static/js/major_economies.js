var myChart = echarts.init(document.getElementById('main'));
var data = [{
    "time": 2017,
    "data": [{
        "name": "United States",
        "value": [2408476, 13.40, "美国"]
    },
    {
        "name": "China",
        "value": [1843792, 10.26, "中国"]
    },
    {
        "name": "Germany",
        "value": [1162907, 6.47, "德国"]
    },
    {
        "name": "Japan",
        "value": [672096, 3.74, "日本"]
    },
    {
        "name": "United Kingdom",
        "value": [641002, 3.57, "英国"]
    },
    {
        "name": "France",
        "value": [619334, 3.45, "法国"]
    },
    {
        "name": "Hong Kong, China",
        "value": [588913, 3.18, "中国香港"]
    },
    {
        "name": "Netherlands",
        "value": [574646, 3.20, "荷兰"]
    },
    {
        "name": "Korea",
        "value": [478478, 2.66, "韩国"]
    },
    {
        "name": "Italy",
        "value": [453122, 2.52, "意大利"]
    }
    ]
},
{
    "time": 2018,
    "data": [{
        "name": "United States",
        "value": [2614221, 13.19, "美国"]
    },
    {
        "name": "China",
        "value": [2135748, 10.78, "中国"]
    },
    {
        "name": "Germany",
        "value": [1284353, 6.48, "德国"]
    },
    {
        "name": "Japan",
        "value": [748488, 3.78, "日本"]
    },
    {
        "name": "France",
        "value": [676441, 3.41, "法国"]
    },
    {
        "name": "United Kingdom",
        "value": [672450, 3.39, "英国"]
    },
    {
        "name": "Netherlands",
        "value": [645502, 3.25, "荷兰"]
    },
    {
        "name": "Hong Kong, China",
        "value": [626616, 3.16, "中国香港"]
    },
    {
        "name": "Korea",
        "value": [535202, 2.70, "韩国"]
    },
    {
        "name": "India",
        "value": [514464, 2.60, "印度"]
    }
    ]
},
{
    "time": 2019,
    "data": [{
        "name": "United States",
        "value": [2567445, 13.27, "美国"]
    },
    {
        "name": "China",
        "value": [2078386, 10.74, "中国"]
    },
    {
        "name": "Germany",
        "value": [1233978, 6.38, "德国"]
    },
    {
        "name": "Japan",
        "value": [720957, 3.73, "日本"]
    },
    {
        "name": "United Kingdom",
        "value": [696208, 3.60, "英国"]
    },
    {
        "name": "France",
        "value": [654658, 3.38, "法国"]
    },
    {
        "name": "Netherlands",
        "value": [635678, 3.29, "荷兰"]
    },
    {
        "name": "Hong Kong, China",
        "value": [577834, 2.99, "中国香港"]
    },
    {
        "name": "Korea",
        "value": [503343, 2.60, "韩国"]
    },
    {
        "name": "India",
        "value": [486059, 2.51, "印度"]
    }
    ]
},
{
    "time": 2020,
    "data": [{
        "name": "United States",
        "value": [2406932, 13.46, "美国"]
    },
    {
        "name": "China",
        "value": [2065964, 11.55, "中国"]
    },
    {
        "name": "Germany",
        "value": [171782, 6.55, "德国"]
    },
    {
        "name": "United Kingdom",
        "value": [638251, 3.57, "英国"]
    },
    {
        "name": "Japan",
        "value": [635460, 3.55, "日本"]
    },
    {
        "name": "Netherlands",
        "value": [595122, 3.32, "荷兰"]
    },
    {
        "name": "France",
        "value": [581297, 3.25, "法国"]
    },
    {
        "name": "Hong Kong, China",
        "value": [569769, 3.19, "中国香港"]
    },
    {
        "name": "Korea",
        "value": [467633, 2.62, "韩国"]
    },
    {
        "name": "Italy",
        "value": [426867, 2.39, "意大利"]
    }
    ]
},
{
    "time": 2021,
    "data": [{
        "name": "United States",
        "value": [2935314, 12.99, "美国"]
    },
    {
        "name": "China",
        "value": [2686747, 11.89, "中国"]
    },
    {
        "name": "Germany",
        "value": [1421512, 6.29, "德国"]
    },
    {
        "name": "Japan",
        "value": [768976, 3.40, "日本"]
    },
    {
        "name": "Netherlands",
        "value": [757380, 3.35, "荷兰"]
    },
    {
        "name": "France",
        "value": [715082, 3.16, "法国"]
    },
    {
        "name": "Hong Kong, China",
        "value": [712358, 3.15, "中国香港"]
    },
    {
        "name": "United Kingdom",
        "value": [694635, 3.07, "英国"]
    },
    {
        "name": "Korea",
        "value": [615093, 2.72, "韩国"]
    },
    {
        "name": "India",
        "value": [573092, 2.54, "印度"]
    }
    ]
},
{
    "time": 2022,
    "data": [{
        "name": "United States",
        "value": [3375819, 13.15, "美国"]
    },
    {
        "name": "China",
        "value": [2716151, 10.58, "中国"]
    },
    {
        "name": "Germany",
        "value": [1570752, 6.11, "德国"]
    },
    {
        "name": "Netherlands",
        "value": [898310, 3.50, "荷兰"]
    },
    {
        "name": "Japan",
        "value": [897242, 3.50, "日本"]
    },
    {
        "name": "United Kingdom",
        "value": [823936, 3.20, "英国"]
    },
    {
        "name": "France",
        "value": [818260, 3.18, "法国"]
    },
    {
        "name": "Korea",
        "value": [737370, 2.85, "韩国"]
    },
    {
        "name": "India",
        "value": [720441, 2.80, "印度"]
    },
    {
        "name": "Italy",
        "value": [689256, 2.68, "意大利"]
    }
    ]
},

]

var option = {
    baseOption: {
        animationDurationUpdate: 1000,
        animationEasingUpdate: 'quinticInOut',
        timeline: {
            axisType: 'category',
            orient: 'vertical',
            autoPlay: true,
            inverse: true,
            playInterval: 5000,
            left: null,
            right: 5,
            top: 20,
            bottom: 20,
            width: 46,
            height: null,
            label: {
                normal: {
                    textStyle: {
                        color: '#222'
                    }
                },
                emphasis: {
                    textStyle: {
                        color: '#000'
                    }
                }
            },
            symbol: 'none',
            lineStyle: {
                color: '#555'
            },
            checkpointStyle: {
                color: '#bbb',
                borderColor: '#777',
                borderWidth: 1
            },
            controlStyle: {
                showNextBtn: false,
                showPrevBtn: false,
                normal: {
                    color: '#666',
                    borderColor: '#666'
                },
                emphasis: {
                    color: '#aaa',
                    borderColor: '#aaa'
                }
            },
            data: data.map(function (ele) {
                return ele.time
            })
        },
        backgroundColor: '#fff',
        title: {
            text: '',
            subtext: '',
            left: 'center',
            top: 'top',
            textStyle: {
                fontSize: 25,
                color: 'rgba(255,255,255, 0.9)'
            }
        },
        tooltip: {
            formatter: function (params) {
                if ('value' in params.data) {
                    return params.data.value[2] + ': ' + params.data.value[0];
                }
            }
        },
        grid: {
            left: '12%',
            right: '45%',
            top: '70%',
            bottom: 20
        },
        xAxis: {},
        yAxis: {},
        series: [{
            id: 'map',
            type: 'map',
            mapType: 'world',
            top: '10%',
            bottom: '25%',
            left: 10,
            itemStyle: {
                normal: {
                    areaColor: '#f0f0f0',
                    borderColor: '#404a59'
                },
                emphasis: {
                    label: {
                        show: true
                    },
                    areaColor: 'rgba(255,255,255, 0.5)'
                }
            },
            data: []
        }, {
            id: 'bar',
            type: 'bar',
            tooltip: {
                show: false
            },
            label: {
                normal: {
                    show: true,
                    position: 'right',
                    textStyle: {
                        color: '#222'
                    }
                }
            },
            data: []
        }, {
            id: 'pie',
            type: 'pie',
            radius: ['8%', '20%'],
            center: ['75%', '85%'],
            roseType: 'radius',
            tooltip: {
                formatter: '{b} {d}%'
            },
            data: [],
            label: {
                normal: {
                    textStyle: {
                        color: '#222'
                    }
                }
            },
            labelLine: {
                normal: {
                    lineStyle: {
                        color: '#ddd'
                    }
                }
            },
            itemStyle: {
                normal: {
                    borderColor: 'rgba(0,0,0,0.3)',
                    borderSize: 1
                }
            }
        }]
    },
    options: []
}

for (var i = 0; i < data.length; i++) {
    var restPercent = 100;
    var restValue = 0;
    data[i].data.forEach(function (ele) {
        restPercent = restPercent - ele.value[1];
    });
    restValue = data[i].data[0].value[0] * (restPercent / data[i].data[0].value[1]);
    console.log(restPercent);
    console.log(restValue);
    option.options.push({
        visualMap: [{
            dimension: 0,
            left: 10,
            itemWidth: 12,
            min: data[i].data[9].value[0],
            max: data[i].data[0].value[0],
            text: ['High', 'Low'],
            textStyle: {
                color: '#222'
            },
            inRange: {
                color: ['lightskyblue', 'yellow', 'orangered', 'red']
            }
        }],
        xAxis: {
            type: 'value',
            boundaryGap: [0, 0.1],
            axisLabel: {
                show: false,
            }
        },
        yAxis: {
            type: 'category',
            axisLabel: {
                textStyle: {
                    color: '#222'
                }
            },
            data: data[i].data.map(function (ele) {
                return ele.value[2]
            }).reverse()
        },
        series: [{
            id: 'map',
            data: data[i].data
        }, {
            id: 'bar',
            data: data[i].data.map(function (ele) {
                return ele.value[0]
            }).sort(function (a, b) {
                return a > b
            })
        }, {
            id: 'pie',
            data: data[i].data.map(function (ele) {
                return {
                    name: ele.value[2],
                    value: ele.value
                }
            }).concat({
                name: '其他国家',
                value: restValue
            }),
        }]
    })
    myChart.setOption(option);
}