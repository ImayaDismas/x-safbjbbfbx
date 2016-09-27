<?php
	//load_ajax.php page
	$host = "localhost";
		    $user = "root";
		    $password = "nyagaka2013";
		    $database_name = "idkeeper";
		    $pdo = new PDO("mysql:host=$host;dbname=$database_name", $user, $password, array(
		    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
		    ));


	$id = trim($_REQUEST['id']);
	$query = $pdo->prepare("select * from group_data JOIN train_data ON group_data.id = train_data.group_id where group_data.id LIKE '%$id%' ORDER BY group_data.id DESC LIMIT 0 , 10");
	$query->bindValue(1, "%$id%", PDO::PARAM_STR);
	$query->execute();
	while ($results = $query->fetch()) {
		$id = $row['id'];
				    echo "<div class=\"row small-up-2 be_wrapper\">";
				     echo "<div class=\"column\">";
					   echo '<img height="150" width="150" class=\"thumbnail\" src="'.$results['image'].'" />';
					   
				     echo "</div>";
				     echo "<div class=\"column\">";
					  echo "<br/>";
					  echo "<strong><h5>  " .$results['first_name'] . "  " .$results['last_name']. "</strong></h5>";
					  echo $results['gender'];
					  echo "<br/>";
					  echo $results['phone_no'];
					  echo "<br/>";
					  echo $results['email'];
					  echo "<br>";
					  echo $results['place'];
					  echo "<br/>";
					  echo "<strong>Group: </strong>".$results['groups'];
					   
				    //more button
				    echo "<form action=\"more_info.php\" method=\"post\">";
					echo '<input  type="hidden" name="more" value="'.$results['id'].'"/>';
					echo "<button type=\"submit\" id=\"button\" value=\"Search\">More Info</button>";
				    echo "</form>";
				    //end more button
				    echo "</div>";
				echo "</div>";
				echo "<br/><br/>";
				    } if(mysql_num_rows($query)==10){?>
		<div id="more<?php echo $id;?>" class="pmc_loadbox">
			<a href="javascript:void(0)" class="more" id="<?php echo $id;?>">more</a>
			<img src="loading.gif" id="loader" style="display:none">
		</div>
		<?php 
	} else {?>
		<div id="more<?php echo $id;?>" class="pmc_loadbox">
			<a>No record...</a>
		</div>
<?php } ?>
