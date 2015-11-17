
while true; do
	ping -t 3 google.com | awk -v host=google.com -v date="$(date)" '/round-trip/ {print date, "|", host, "|", $4}' >> stdms.txt
	sleep 5
done

