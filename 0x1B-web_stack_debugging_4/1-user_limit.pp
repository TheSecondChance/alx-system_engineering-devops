# Thsi for Changes the OS configuration that it is possible to login with the alx user
# and open a file without any error message
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
