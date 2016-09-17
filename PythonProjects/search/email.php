<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="x-ua-compatible" content="ie=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ID KEEPER</title>
<link href="http://fonts.googleapis.com/css?family=Crete+Round" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="css/foundation.css">
<link rel="stylesheet" href="foundation-icons/foundation-icons.css" />
<link rel="stylesheet" href="css/app.css">
    
</head>
    <body>   
   
   <!-- Start Top Bar -->
    <div class="top-bar">
      <div class="row">
        <div class="top-bar-left">
          <ul class="dropdown menu" data-dropdown-menu>
            <li><a onclick="history.back(-1)" ><i class="fi-arrow-left"></i></a></li>
            <li><a href="index.html"><i class="fi-home"></i></a></li>
            <li class="menu-text"><h1><a href="results.php">Search Results</a></h1></li>
          </ul>
        </div>
      </div>
    </div>
    <!-- End Top Bar -->

<!--    main content section-->
   <div class="row">
        
        <?php 

		//load database connection
		    $host = "localhost";
		    $user = "root";
		    $password = "nyagaka2013";
		    $database_name = "idkeeper";
		    $pdo = new PDO("mysql:host=$host;dbname=$database_name", $user, $password, array(
		    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
		    ));

		// Search from MySQL database table
		$email=$_POST['email'];
		$query = $pdo->prepare("select * from train_data INNER JOIN topic_data ON train_data.topic_id = topic_data.id INNER JOIN group_data ON train_data.group_id = group_data.id where train_data.email LIKE '%$email%'  LIMIT 0 , 100");
		$query->bindValue(1, "%$email%", PDO::PARAM_STR);
		$query->execute();

		// Display search result
			 if (!$query->rowCount() == 0) {
				//echo "Search found :<br/>";             
			    while ($results = $query->fetch()) {  
				echo "<div class=\"medium-6 columns one\">";
					echo "<div class=\"be_wrapper\">";
					echo "<div class=\"row small-up-3\">";
					    echo "<div class=\"column\">";
						echo '<img height="300" width="300" class=\"thumbnail\" src="'.$results['image'].'" />';
						//echo "<button id=\"button\">Change Image</button>";
					    echo "</div>";
					    echo "<div class=\"column\">";
						echo '<img height="300" width="300" class=\"thumbnail\" src="'.$results['image'].'" />';
						//echo "<button id=\"button\">Change Image</button>";
					    echo "</div>";
					    echo "<div class=\"column\">";
						echo '<img height="300" width="300" class=\"thumbnail\" src="'.$results['image'].'" />';
						//echo "<button id=\"button\">Change Image</button>";
					    echo "</div>";
					    echo "<button id=\"button\">Change Image</button>";
					   echo "</div>";
					echo "</div>";					   
				echo "</div>"; 
				echo "<div class=\"medium-6 large-5 columns\">";
					echo "<div class=\"be_wrapper\">";
					  echo "<strong><h5>  " .$results['first_name'] . "  " .$results['last_name']. "</strong></h5>";
					  echo $results['gender'];
					  echo "<br/>";
					  echo $results['phone_no'];
					  echo "<br/>";
					  echo $results['email'];
					  echo "<br/>";
					  echo $results['place'];
                                          echo "<br/>";
			                  echo "<strong>Group: </strong>".$results['groups'];
					  echo "<br/>";
					  echo "<strong>Topic: </strong>".$results['topic'];
					  echo "<div class=\"row small-up-2\">";
					    echo "<div class=\"column\">";
							echo "<button id=\"button\">CHECK FOR UPDATES</button>";
					    echo "</div>";
					    echo "<div class=\"column\">";
							echo "<button id=\"button\">SAVE</button>";
					    echo "</div>";
					echo "</div>";
				   echo "</div>";
				echo "</div>";
                    echo "<br/><br/>"; 
				    }

			} else {
			    echo 'ERROR: No such number found';
			}
		?>
    </div>

<!--    end of main content section-->
     
<!--      footer -->

<div class="row column footer1">
<hr>
    All rights reserved, Developed by <strong>Synergetic</strong>.
</div>

<!--     end of footer   -->
<!--        Scripts-->
    <script src="js/vendor/jquery.js"></script>
    <script src="js/vendor/what-input.js"></script>
    <script src="js/vendor/foundation.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
