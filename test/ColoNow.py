from datetime import datetime, timedelta

# Stringa di data e ora nel formato ISO 8601
iso_string = "2024-01-25T14:45:00.000Z"

# Converti la stringa in un oggetto datetime
datetime_obj = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))

# Sottrai una settimana
one_week_ago = datetime_obj - timedelta(weeks=1)

# Formatta la data e l'ora nel formato desiderat0
iso_string = one_week_ago.isoformat().replace("+00:00","Z")

print(iso_string)
