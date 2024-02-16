# find out why Apache is returning a 500 error
exec { 'remove typo':
    cwd     => '/var/www/html',
    command => '/bin/sed -i -e "s/.phpp/.php/g" wp-settings.php',
}

