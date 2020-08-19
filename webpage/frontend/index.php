<?php

if (isset($_POST['form-submit'])) {
    // warn user about the errors and kill function
    function problem($error)
    {
        echo "<script type='text/javascript'>alert('$error');</script>";
        die();
    }

    // check if there is injection in form
    function IsInjected($str){
        $injections = array('(\n+)',
            '(\r+)',
            '(\t+)',
            '(%0A+)',
            '(%0D+)',
            '(%08+)',
            '(%09+)'
        );

        $inject = join('|', $injections);
        $inject = "/$inject/i";

        if(preg_match($inject,$str))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    // TODO: This needs to be changed to get the value from the DB
    $to_email = "ivofdcarvalho@gmail.com";

    // validation expected data exists
    if (!isset($_POST['form-name']) || !isset($_POST['form-email']) || !isset($_POST['form-subject']) || !isset($_POST['form-message'])){
        problem('We are sorry, but there appears to be a problem with the form you submitted.');
    }

    $name = $_POST['form-name'];
    $from_email = $_POST['form-email'];
    $subject = $_POST['form-subject'];
    $message = $_POST['form-message'];

    // check for injection
    if(IsInjected($to_email) || IsInjected($name) || IsInjected($from_email) || IsInjected($subject) || IsInjected($message)){
        problem('We are sorry, but there form cannot be submitted with the data provided.');
    }

    $message_email = "Form details below.\r\n";
    $message_email .= "Name: $name \r\n";
    $message_email .= "Email: $from_email \r\n";
    $message_email .= "Message: $message \r\n";

    @mail($to_email, $subject, $message_email);

    echo "<script type='text/javascript'>alert('Thank you for the contact. We will be in touch with you very soon.');window.location.href='index.html'</script>";
}