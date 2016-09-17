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
            <li class="menu-text"><h1><a href= "results.html">Search Results</a></h1></li>
          </ul>
        </div>
      </div>
    </div>
    <!-- End Top Bar -->
    
    <br>

<!--    main content section-->
    <div class="row">
    <div class="medium-6 columns">
        <img class="thumbnail" src="http://placehold.it/650x350">
        <div class="row small-up-4">
            <div class="column">
                <img class="thumbnail" src="http://placehold.it/250x200">
            </div>
            <div class="column">
                <img class="thumbnail" src="http://placehold.it/250x200">
            </div>
            <div class="column">
                <img class="thumbnail" src="http://placehold.it/250x200">
            </div>
            <div class="column">
                <img class="thumbnail" src="http://placehold.it/250x200">
            </div>
        </div>
    </div>
    <div class="medium-6 large-5 columns">

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
$search=$_POST['search'];
$query = $pdo->prepare("select * from train_data where first_name LIKE '%$search%' OR last_name LIKE '%$search%'  LIMIT 0 , 100");
$query->bindValue(1, "%$search%", PDO::PARAM_STR);
$query->execute();

// Display search result
         if (!$query->rowCount() == 0) {
                //echo "Search found :<br/>";
                echo "<h3 style=\"text-align:center;\">Results Found</h3>";             
            while ($results = $query->fetch()) {  
                echo "<div class=\"row small-up-2\">";
		     echo "<div class=\"column\">";
			   echo '<img height="300" width="300" class=\"thumbnail\" src="'.$results['image'].'" />';
		           
		     echo "</div>";
		     echo "<div class=\"column\">";
			  echo "<br/><br/>";
		          echo "<strong>Name:</strong>". "  " .$results['first_name'] . "  " .$results['last_name'];
		          echo "<br/>";
		          echo "<strong>Phone:</strong>". "  " .$results['phone_no'];
		          echo "<br/>";
		          echo "<strong>Email: </strong>". "  " .$results['email'];
		          echo "<br/>";
		          echo "<strong>Location: </strong>". "  " .$results['place'];
		          echo "<br/><br/>"; 
	//                echo $results['email'];
		    echo "</div>";
		echo "</div>";                
		    }

        } else {
            echo 'Nothing found';
        }
?>
        <!-- <p><strong>Name: </strong>Imaya Dismas</p>
        <p>Alias: Dc, Nyagaka</p>
        <p><strong>Phone: </strong>0700415505</p>
        <p><strong>Location: </strong>Chiromo, Nairobi</p>
        <p><strong>Email: </strong>imayadismas@gmail.com</p>
        <p><strong>Group: </strong>Nairobi Twitter Developer Community</p>
        <p><strong>Topic: </strong>Software Development</p>
        <p><strong>Bio: </strong>Software Development</p> -->
        
        <div class="row small-up-2">
            <div class="column">
                        <button id="button">CHECK FOR UPDATES</button>
            </div>
            <div class="column">
                        <button id="button">SAVE</button>
            </div>
        </div>
    </div>
</div>

<!--    end of main content section-->
     
<!--      footer -->

<div class="row column footer">
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
