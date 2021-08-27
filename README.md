# Anomaly-Detection-in-IoT-Sensor-Networks
Detect anomalies in Industrial IoT Pump Sensor Network


<b>Node-Red Implementation</b><br>
<ol>
<li>We have implemented node red flows using the node-red-contrib-machine-learning v2 packages that allows for implementing machine learning models in pickled form or creating it from scratch. </li>
<li>The load dataset function allows us to load a dataset in csv format from the local machine and pass it on for further analysis. </li>
<li>Using MQTT or other nodes that allows for communication between client and server instances we can communicate the dataset to the server. </li>
<li>The prediction node Anomaly_Detection imports the model generated from the python script and contains the serialized object of the anomaly detection model in a pickled model.</li> 
<li>The predictions will be printed on the server side, or an additional MQTT node can be added to communicate back the results back to the client.</li>
</ol>
