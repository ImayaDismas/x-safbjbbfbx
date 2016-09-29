$def with (form, text)


<!DOCTYPE html>
<html ng-app="IdKeeperApp">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">

    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    <link rel="stylesheet" type="text/css" href="/static/tutorial.css" />
    <script type="text/javascript" src="/static/jquery.js"></script>
     <script type="text/javascript">
        jQuery(document).ready(function () {
            jQuery(".button").click(function () {
                var input_string = $$("input#name").val();
                jQuery.ajax({
                    type: "POST",
                    data: {
                        name: input_string
                    },
                    success: function (data) {
                        jQuery('#foo').html(data).hide().fadeIn(1500);
                    },
                });
                return false;
            });
        });
    </script>
</head>

<body ng-controller="IdKeeperCtrl">

    <div data-role="page" id="pageone">

        <div data-role="header" class="header">

           <div class="ui-grid-b ui-responsive">
               <div class="ui-block-a">
               </div>
               <div class="ui-block-b">
                   <h1>ID KEEPER</h1>
               </div>
                <div class="ui-block-c">
                </div>
            </div>

        </div>

        <div data-role="main" class="ui-content">
           <div class="ui-grid-b ui-responsive">
             <div class="ui-block-a">
             </div>
              <div class="ui-block-b">
                   <form method="post" class="form">
                        <p>Search Page</p>
                        <input type="search" name="name"  id="name" placeholder="Search..." />
                        <input class="button" type="submit" value="Search"/>
                        <input type="button" value="Create Files" onclick="exec('./idkeeper.py');" />
                  </form>
                 <br>
                 <br>
                 <span id="foo">$text</span>

              </div>
              <div class="ui-block-c">
             </div>
            </div>

        </div>

        <div class="footer" data-role="footer">
           <div class="ui-grid-b ui-responsive">
               <div class="ui-block-a">
               </div>
               <div class="ui-block-b">
                   <h4>Developed by Synergetic, All rights reserved</h4>
               </div>
                <div class="ui-block-c">
                </div>
           </div>
        </div>
    </div>
    <div data-role="page" id="pagetwo">
        <div data-role="header">
            <h1>ID KEEPER</h1>

        </div>

        <div class="ui-grid-b ui-responsive">
             <div class="ui-block-a">
             </div>
              <div class="ui-block-b">
                    <p>Search Results</p>
                    <a href="#pageone" class="ui-btn ui-btn-inline">Go to Page One</a>
                    <a href="#pagethree" class="ui-btn ui-btn-inline ui-btn-b">View More</a>
              </div>
              <div class="ui-block-c">
             </div>
            </div>

        <div class="footer" data-role="footer">
            <h1>Developed by Synergetic, All rights reserved</h1>
        </div>
    </div>

    <div data-role="page" data-dialog="true" id="pagethree">
        <div data-role="header" data-theme="b">
            <h1>Search Results</h1>
        </div>

        <div data-role="main" class="ui-content">
            <p>I'm A Themed Dialog Box - My Header And Footer Is Black!</p>
            <a href="#pagetwo" class="ui-btn ui-btn-inline">Go to Page Two</a>
        </div>

        <div data-role="footer" data-theme="b">
            <h1>&copy;Synergetic Limited</h1>
        </div>
    </div>

    <script type="text/javascript" src="/static/jquery.js"></script>
     <script>


    </script>


</body>

</html>
