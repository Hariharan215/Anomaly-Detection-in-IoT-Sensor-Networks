# Anomaly-Detection-in-IoT-Sensor-Networks
Detect anomalies in Industrial IoT Pump Sensor Network

In our project, we consider an industrial pump sensor network. The network consists of multiple nodes of the same type. The main nodes in the network measures pressure of the water that is flowing through the pipes at different locations in which it is deployed. Other nodes collect auxiliary details such as location etc. A centralized controller also exists which can divert water as per requirement even in case breaches are detected through an alternate route. In case there is any failures of nodes that cannot be fixed, the controller will raise “broken” flag. Then it may go into “recovering” state before it becomes “normal”. 

</b>Modules</b><br>

![mainmenu](/samples/iotproj.PNG)<br>

<b>Exploratory Data Analysis</b><br>

![mainmenu](/samples/head.PNG)<br>

Sensor timeseries plot example:

![mainmenu](/samples/sensorplot.PNG)<br>

<b>Node-Red Implementation</b><br>
<ul>
<li>We have implemented node red flows using the node-red-contrib-machine-learning v2 packages that allows for implementing machine learning models in pickled form or creating it from scratch. </li>
<li>The load dataset function allows us to load a dataset in csv format from the local machine and pass it on for further analysis. </li>
<li>Using MQTT or other nodes that allows for communication between client and server instances we can communicate the dataset to the server. </li>
<li>The prediction node Anomaly_Detection imports the model generated from the python script and contains the serialized object of the anomaly detection model in a pickled model.</li> 
<li>The predictions will be printed on the server side, or an additional MQTT node can be added to communicate back the results back to the client.</li>
</ul><br>

![mainmenu](/samples/nodered1.PNG)<br>

The following is an alternate flow that demonstrates the capabilities of the machine learning package that allows us to train the model in node-red environment itself. In this case we have trained a decision tree classifier completely within node-red environment. Assesment and predictor nodes are available that allows us to see the results. 
![mainmenu](/samples/nodered2.PNG)<br>

Flow for generating a random record for testing (record is stored in CSV file which can be imported in node red and passed to predictor for testings):

![mainmenu](/samples/nodered3.PNG)<br>


