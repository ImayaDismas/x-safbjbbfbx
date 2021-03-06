<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="x-ua-compatible" content="ie=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ID KEEPER</title>
<link href="http://fonts.googleapis.com/css?family=Crete+Round" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="../css/foundation.css">
<link rel="stylesheet" href="../foundation-icons/foundation-icons.css" />
<link rel="stylesheet" href="../css/app.css">
    
</head>
    <body>
<!--        Body-->
   <div id="page-wrap">
         
    <section id="main-content">
    <div id="guts"> 
    
     <!-- Start Top Bar -->
    <div class="top-bar1">
      <div class="row">
        <div class="top-bar-left">
          <ul class="dropdown menu" data-dropdown-menu>
            <li><a href="index.html"><i class="fi-home"></i></a></li>
<!--            <li class="menu-text"><h3>Search by Multiple Options</h3></li>-->
          </ul>
        </div>
      </div>
    </div>
    <!-- End Top Bar -->
    
    <div class="row medium-6 large-5 columns">
        <div class="blog-post">
            <div class="row small-up-3">
              <div class="column multiple">
                    <i class="fi-telephone"></i>
              </div>
               <div class="column move">
                   <input id="checkbox1" type="checkbox"/>
               </div>
                <div class="column move">
                    <form class="search_bar small">
                        <input type="text" placeholder="Enter mobile number" />
                    </form>
                </div>
            </div>
        </div>
    </div>
    

    
    <div class="row medium-6 large-5 columns">
        <div class="blog-post">
           <div class="row small-up-3">
              <div class="column">
                  <i class="fi-marker"></i>
              </div>
               <div class="column">
                    <input id="checkbox2" type="checkbox"/>
                </div>
                <div class="column">
                    <form class="search_bar small">
                        <input type="text" placeholder="Enter location" />
                    </form>
                </div>
            </div>
        </div>
    </div>
    
    
    
    <div class="row medium-6 large-5 columns">
        <div class="blog-post">
           <div class="row small-up-3">
              <div class="column">
                  <i class="fi-mail"></i>
              </div>
               <div class="column">
                    <input id="checkbox3" type="checkbox"/>
                </div>
                <div class="column">
                    <form class="search_bar small">
                        <input type="text" placeholder="Enter email address" />
                    </form>
                </div>
            </div>
        </div>
    </div>
    
   
    
    <div class="row medium-6 large-5 columns">
        <div class="blog-post">
            <div class="row small-up-3">
              <div class="column">
                  <i class="fi-torso"></i>
              </div>
               <div class="column">
                    
                    <input id="checkbox4" type="checkbox"/>
                </div>
                <div class="column">
                    <form class="search_bar small">
                        <input type="text" placeholder="Enter name" />
                    </form>
                </div>
            </div>
        </div>
    </div>
    
    
    
    <div class="row medium-6 large-5 columns">
        <div class="blog-post">
            <div class="row small-up-3">
               <div class="column">
                  <i class="fi-torsos-all"></i>
              </div>
               <div class="column">
                    <input id="checkbox5" type="checkbox"/>
                </div>
                <div class="column drop">
                     
                      <select>
                        <option>Choose Group</option>
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
			    $query = $pdo->prepare("select groups from group_data  LIMIT 0 , 10");
			    $query->execute();
			    // Display search result
			    if (!$query->rowCount() == 0) {
				while ($results = $query->fetch()) {
					echo "<option>".$results['groups']."</option>";
				}
			    
			    }				
			    ?>
                      </select>
                      
                </div>
            </div>
        </div>
    </div>
    
    
    
    <div class="row medium-6 large-5 columns">
        <div class="blog-post">
            <div class="row small-up-3">
               <div class="column">
                  <i class="fi-text-color"></i>
              </div>
               <div class="column">
                    <input id="checkbox6" type="checkbox"/>
                </div>
                <div class="column drop">
                     
                      <select>
                        <option>Choose Topic</option>
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
			    $query = $pdo->prepare("select topic from topic_data  LIMIT 0 , 10");
			    $query->execute();
			    // Display search result
			    if (!$query->rowCount() == 0) {
				while ($results = $query->fetch()) {
					echo "<option>".$results['topic']."</option>";
				}
			    
			    }				
			    ?>
                      </select>
                      
                </div>
            </div>
        </div>
    </div>
    
    <br>
    
    <div class="row medium-6 large-5 columns">
        <button class ="align-button" id="button">Search</button>
    </div>
    
    </div>
    </section>    

<!--      footer -->
    <div class="row column footer1">
    <hr>
        All rights reserved, Developed by <strong>Synergetic</strong>.
    </div>    
<!--     end of footer   -->
<!--        Scripts-->
    <script src="../js/vendor/jquery.js"></script>
    <script src="../js/vendor/what-input.js"></script>
    <script src="../js/vendor/foundation.js"></script>
    <script src="../js/app.js"></script>
    </div>
    </body>        
</html>

