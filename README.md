# Covid-19-Data-API
This is an API which gives the following data about the Covid-19:
1. The top 5 countries with most recovered per capita, in the last 10 days
2. The average recovered cases per 100 square KM per country since the pandemic began.
3. The top 10 countries recovered cases in the last week.

<p>The project uses the next free API service to get the data. <a href="https://github.com/M-Media-Group/Covid-19-API">https://github.com/M-Media-Group/Covid-19-API</a></p>
<p>The project uses AWS Lambda function, and an Amazon API Gateway endpoint to trigger that function.</p>
<p>Guide about how to create a simple microservice using Lambda and API Gateway
 <a href="https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-blueprint.html">https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-blueprint.html</a></p>

# How to us it?

<p>Example request:<br>GET <a rel="noreferrer noopener" href="https://ozmka0n96a.execute-api.eu-west-2.amazonaws.com/default/Covid-19-Data-API" target="_blank">https://ozmka0n96a.execute-api.eu-west-2.amazonaws.com/default/Covid-19-Data-API</a></p>

Example response:
```
{
  "Top_5_countries_with_most_recovered_per_capita_last_10_days": {
    "1": {
      "country": "Seychelles",
      "recovered_per_capita": 0.02288440630376727
    },
    "2": {
      "country": "Holy See",
      "recovered_per_capita": 0.012
    },
    ......
    ......
    ......
    "5": {
      "country": "Hungary",
      "recovered_per_capita": 0.007110382192814959
    }
  },
  "The_average_recovered_cases_per_100_square_KM_per_country": {
    "Afghanistan": {
      "recovered_cases_per_100_square_KM": 8.555567483016148
    },
    "Albania": {
      "recovered_cases_per_100_square_KM": 446.7267288159176
    },
    ......
    ......
    ......
  },
  "The_top_10_countries_recovered_cases_in_the_last_week": {
    "1": {
      "country": "India",
      "recovered_in_last_week": 2275030
    },
    "2": {
      "country": "Brazil",
      "recovered_in_last_week": 392978
    },
    ......
    ......
    ......
    "10": {
      "country": "Russia",
      "recovered_in_last_week": 52622
    }
  }
}
```

Countries without enough information:
<ul>
  <li>Burma</li>
  <li>Cabo Verde</li>
  <li>Congo (Brazzaville)</li>
  <li>Diamond Princess</li>
  <li>Eswatini</li>
  <li>Kosovo</li>
  <li>MS Zaandam</li>
  <li>Micronesia</li>
  <li>Montenegro</li>
  <li>Serbia</li>
  <li>Taiwan</li>
  <li>Timor-Leste</li>
  <li>West Bank and Gaza</li>
</ul>
