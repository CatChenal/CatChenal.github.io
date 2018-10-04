BEGIN
{ m=split("Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec", d ,"|")
   for(i=1; i<=m; i++) {
    months[d[i]]=sprintf("%02d", i)
    }
  dt_frmt = "%Y-%m-%d"
}
{ name=$9; 
   for (i=9; i<=NF; i++) { 
    name=sprintf("%s_%s", name, $i)
    }; 
    printf("%i-%s-%02d-%s\n", $8, $6, $7, name) 
   }
 }