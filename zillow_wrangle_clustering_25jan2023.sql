
select *, distinct prop.id
from properties_2017 as prop
join predictions_2017 USING(parcelid)
join propertylandusetype USING(propertylandusetypeid)
where propertylandusetypeid = 261; 
