  GNU nano 5.8                                                                               New Buffer                                                                               Modified
#!/bin/bash

if [[ $# -ne 1 ]]; then
  echo "Usage:" $0 "correos"
  exit 1
fi

for email in $(cat $1)
do
  echo $email

  curl -s -A "CloudSavvyIT" \
  -H "237d199916384e0aaef2a6508410d82b" \
  https://haveibeenpwned.com/api/v3/breachedaccount/$email?truncateResponse=false \
  | jq -j '.[] | " ", .Title, " [", .Name, "] ", .BreachDate, "\n"'

  echo "---"
  sleep 1.6
done

exit 0
