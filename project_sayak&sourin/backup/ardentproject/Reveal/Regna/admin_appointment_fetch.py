#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
cur.execute("SELECT * FROM appointment where status='p'" )
x=cur.fetchall()
db.commit()
print("""
		<html>
		<head>
        <input type="button" class="button" value="&#8592; Back" onclick="history.back()">
        
        <meta charset="UTF-8">
		 <title>Appointments</title>
		<h2>NEW APPOINTMENTS</h2>
        <style>
        
        .button {
  background-color: #080794; /* Blue */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

#customers {
  font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #080794;
  color: white;
}
</style>
</head>
		<body>
		
		<table id="customers">
		<thead>
        <th>SL</th>
		<th>Name</th>
		<th>Phone</th>
        <th>Email</th>
        <th>Age</th>
        <th>Gender</th>
        <th>Date of Appointment</th>
        </thead>
		<tbody>

""")
for i in range(len(x)):
    print("""
		
		<tr>
		<td>{0}</td>
		<td>{1}</td>
        <td>{2}</td>
        <td>{3}</td>
        <td>{4}</td>
        <td>{5}</td>
        <td>{6}</td>
        </tr>
		
		
		
	""".format(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4],x[i][5],x[i][7]))
    
print("""
		</tbody>
        </table>
		
		</body>
		</html>
	""")
print("""
<html>
<style>

        
        form { 
margin: 0 auto; 
width:500px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

input[type=number] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
        
        
</style>  

<body>
<form action="appointment_update.py" method="post">
<br/><br/><br/>Enter SL No. to provide Appointment <input type="number" name="sl"> <input type="submit" value="UPDATE">
</form>
</body>
</html>
""")