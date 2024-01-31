var line1=echarts.init(document.getElementById('line1'));
var line2=echarts.init(document.getElementById('line2'));
var data={};
function getDataline(countryname){
    var selectedStart = $('#start').val();
    var selectedEnd = $('#end').val();
    var startmonth=$('#startmonth').val();
    var endmonth=$('#endmonth').val();
    var Time=[];
    var months=['January','February','March','April','May','June','July','August','September','October','November','December'];
    if(selectedEnd<selectedStart){
        confirm("结束时间必须在开始时间之后！");
        return;
    }else if(selectedStart!=selectedEnd){
        currentyear=Number(selectedStart);
        var num=months.findIndex(element=>element==startmonth);
        for(var i=num;i<12;i++){
            Time.push({'year':currentyear,'month':months[i]});
        }
        currentyear++;
        while(currentyear<selectedEnd){
            for(var i=0;i<12;i++){
            Time.push({'year':currentyear,'month':months[i]});}
            currentyear++;
        }
        num=months.findIndex(element=>element==endmonth);
        for(var i=0;i<num+1;i++){
            Time.push({'year':currentyear,'month':months[i]})
        }
    }else{
        currentyear=Number(selectedStart);
            var num1=months.findIndex(element=>element==startmonth);
            var num2=months.findIndex(element=>element==endmonth);
            if(num1>num2){
                confirm("结束时间必须在开始时间之后！");
                return;
            }else{for(var i=num1;i<num2+1;i++){
                Time.push({'year':currentyear,'month':months[i]});
        }}
    }
    fetch(`/month-data-import/?country=${countryname}`)
    .then(response=>response.json()).then(data=>{
        console.log(data);
        updateimportchart(data,Time);
    }).catch(error=>{
        console.error('Error fetching data:',error);
        alert('未收录该国家数据！')
    });
    fetch(`/month-data-export/?country=${countryname}`)
    .then(response=>response.json()).then(data=>{
        console.log(data);
        updateexportchart(data,Time);
    }).catch(error=>{
        console.error('Error fetching data:',error);
    });
}
function updateimportchart(response,Time){
    line1.clear();
    var data=response.data;
    data=sortby(data,Time);
    var yearoption={
        title: {
            text: 'Import Values Over Months'
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
            data: data.map(element=>{
                return element.year+' '+element.month;
            })
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data:data.map(element=>{
                return element.value;
            }),
            type: 'line',
        }
        ]  // 在这里设置系列，每个指标一个系列项
    };
    
    line1.setOption(yearoption);
}
function updateexportchart(response,Time){
    line2.clear();
    var data=response.data;
    data=sortby(data,Time);
    var yearoption={
        title: {
            text: 'Export Values Over Months'
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
            data: data.map(element=>{
                return element.year+' '+element.month;
            })
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data:data.map(element=>{
                return element.value;
            }),
            type: 'line',
        }
        ]  // 在这里设置系列，每个指标一个系列项
    };
    
    line2.setOption(yearoption);
}
function sortby(data,Time){
    var result=[];
    var timely=data.map(element=>{
        return {'year':element.year,'month':element.month};
    })
    Time.forEach(element => {
        var num=timely.findIndex(temp=>temp.year==element.year&&temp.month==element.month);
        result.push(data[num]);
    });
    return result;
}