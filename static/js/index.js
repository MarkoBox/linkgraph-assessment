function getChartData() {
            const targetUrl = document.getElementById("tradeData").getAttribute("source");
            fetch(targetUrl).then(res => {
                return res.json()
            }).then(data => {
                let label_data = [];
                let chart_data = [];
                data.results.map(x => {
                    chart_data.push(x.weighted_price);
                    label_data.push(x.coin.ticker_symbol);
                })
                generateChart(label_data, chart_data);
            }).catch(error => {
                console.log(error)
            })
        }

        window.onload = function () {
            getChartData();
            //console.log(api_data)
        };

        function generateChart(label_data, chart_data) {


            var ctx = document.getElementById('tradeData').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: label_data,
                    datasets: [{
                        label: 'Weighted Price',
                        data: chart_data,
                        backgroundColor: [
                            "rgb(255, 0, 41)",
                            "rgb(55, 126, 184)",
                            "rgb(102, 166, 30)",
                            "rgb(152, 78, 163)",
                            "rgb(0, 210, 213)",
                            "rgb(255, 127, 0)",
                            "rgb(255, 0, 41)",
                            "rgb(55, 126, 184)",
                            "rgb(102, 166, 30)",
                            "rgb(152, 78, 163)",
                            "rgb(0, 210, 213)",
                            "rgb(255, 127, 0)",
                            "rgb(255, 0, 41)",
                            "rgb(55, 126, 184)",
                            "rgb(102, 166, 30)",
                            "rgb(152, 78, 163)",
                            "rgb(0, 210, 213)",
                            "rgb(0, 210, 213)",
                            "rgb(55, 126, 184)",
                            "rgb(255, 0, 41)"],

                        borderWidth: 1
                    }]
                },

                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }