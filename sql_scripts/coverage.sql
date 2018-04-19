

drop table if exists record_compiled_release;
select ocid, data -> 'compiledRelease' as compiledRelease into record_compiled_release from record join data on record.data_id = data.id;


drop table if exists record_compiled_release_flat;
WITH RECURSIVE all_paths(ocid, path, "value") AS (
    select ocid,
       (key_value).key "path", 
       (key_value).value "value" from 
    (select ocid, jsonb_each(compiledRelease) key_value from record_compiled_release) a
  UNION ALL
    (select ocid,
           case when key_value is not null then
               a.path || '/'::text || (key_value).key::text
           else
               a.path
           end "path",
           case when a.key_value is not null then
               (a.key_value).value
           else
               array_value
           end "value"
     from
        (select 
           ocid,
           path,
           jsonb_each(case when jsonb_typeof(value) = 'object' then value else '{}'::jsonb end) key_value,
           jsonb_array_elements(case when jsonb_typeof(value) = 'array' and jsonb_typeof(value -> 0) = 'object' then value else '[]'::jsonb end) "array_value"
           from all_paths
        ) a
   )
)
SELECT ocid, path into record_compiled_release_flat  
FROM all_paths;



drop TABLE if exists record_compiled_release_field_summary;
select path, count(*) total, count(distinct ocid) processes into record_compiled_release_field_summary from record_compiled_release_flat  group by path;

