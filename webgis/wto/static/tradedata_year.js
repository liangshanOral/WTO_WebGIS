var line1 = echarts.init(document.getElementById('line1'));
var line2 = echarts.init(document.getElementById('line2'));
var worldmap = echarts.init(document.getElementById('worldmap'));
var data = {};
function getDataline(countryname) {
    var selectedStart = $('#start').val();
    var selectedEnd = $('#end').val();
    var Time = [];
    if (selectedEnd < selectedStart) {
        confirm("结束时间必须在开始时间之后！")
        selectedEnd = selectedStart
        currentyear = Number(selectedStart);
        while (currentyear <= selectedEnd) {
            Time.push(currentyear);
            currentyear++;
        }
    } else {
        currentyear = Number(selectedStart);
        while (currentyear <= selectedEnd) {
            Time.push(currentyear);
            currentyear++;
        }
    }
    fetch(`/year-data-import/?country=${countryname}`)
        .then(response => response.json()).then(data => {
            console.log(data);
            updateimportchart(data, Time);
        }).catch(error => {
            console.error('Error fetching data:', error);
            alert("未收录该国家的数据！");
        });
    fetch(`/year-data-export/?country=${countryname}`)
        .then(response => response.json()).then(data => {
            console.log(data);
            updateexportchart(data, Time);
        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    line1.on('click', function (params) {
        if (params.componentType === 'series') {
            var tempyear = Number(params.name);
 
            fetch(`/year-heat-import/?year=${tempyear}`)
                .then(response => response.json()).then(data => {
                    console.log(data);
                    updatemap(data);
                }).catch(error => {
                    console.error('Error fetching data:', error);
                });

        }
    });
    line2.on('click', function (params) {
        if (params.componentType === 'series') {
            var tempyear = Number(params.name);
 
            fetch(`/year-heat-export/?year=${tempyear}`)
                .then(response => response.json()).then(data => {
                    console.log(data);
                    updatemap(data);
                }).catch(error => {
                    console.error('Error fetching data:', error);
                });

        }
    });
}
function updateimportchart(response, Time) {
    line1.clear();
    var data = response.data;
    data = sortby(data, Time);
    var yearoption = {
        title: {
            text: 'Import Values Over Years'
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
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'right',
            top: 'top',
            feature: {
                dataView: { readOnly: false },
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: data.map(item => {
                return item.year;
            })
        },
        legend: {
            data: []  // 在这里设置图例，每个指标一个图例项
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: data.map(item => {
                return item.value;
            }),
            type: 'line',
        }
        ]  // 在这里设置系列，每个指标一个系列项
    };

    line1.setOption(yearoption);
}
function updateexportchart(response, Time) {
    line2.clear();
    var data = response.data;
    data = sortby(data, Time);
    var yearoption = {
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
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: data.map(item => {
                return item.year;
            }),
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: data.map(item => {
                return item.value;
            }),
            type: 'line',
        }
        ]  // 在这里设置系列，每个指标一个系列项
    };

    line2.setOption(yearoption);
}
function sortby(data, Time) {
    var result = [];
    var timely = data.map(element => {
        return element.year;
    })
    Time.forEach(element => {
        var num = timely.findIndex(year => year == element);
        if (num != -1) {
            result.push(data[num]);
        }
    });
    return result;
}
function updatemap(response) {
    worldmap.clear();
    var data = response.data;
    var mapoption = {

        visualMap: {
            min: 75,
            max: 130,
            text: ['High', 'Low'],
            inRange: {
                color: ['lightskyblue', 'yellow', 'orangered']
            }
        },

        series: [{
            type: 'map',
            map: 'world',
            data: data,
            nameMap:{
                'United States':'United States of America',
                'Russia':'Russian Federation',
                'Saudi Arabia':'Saudi Arabia, Kingdom of'
            }
        }]

    }
    worldmap.setOption(mapoption);
}