<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="x-ua-compatible" content="ie=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ID KEEPER</title>

    
</head>
    <body> 
        <?php
            /*
            Error reporting helps you understand what's wrong with your code, remove in production.
            */
            error_reporting(E_ALL); 
            ini_set('display_errors', 1);

            $search=$_POST['search'];

            $read = exec("python test.py user@domain.tld $search");
            if($read == "ok, registered")
                {
                    echo "ok, registered";
                }
            else if($read == "NOT registered")
                {
                    echo "failed";
                }
            ?>
    </body>        
</html>

