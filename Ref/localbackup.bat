:localloadbackup
cls
echo really WIP not worked yet
::You know? Loadbackup is work as offline. this code is totally useless sh1t
for %%z in (%ClientLocation%\SkinTemp\list\*.skin) do (
    set localloadbackuped=%%~nz
    echo !localloadbackuped%
        if not exist  %ClientLocation%\SkinTemp\Zip\%localloadbackuped%.zip (
            echo File not exist in Temp folder!
            goto start
        )
        mkdir %ClientLocation%\skinTemp\Temp
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\american
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\british
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\chinese
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\czech
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\french
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\german
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\japan
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\italy
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\poland
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\russian
        mkdir %ClientLocation%\res_mods\%ClientVersion%\vehicles\sweden

        tar.exe -xf "%ClientLocation%\SkinTemp\zip\%localloadbackuped%.zip" -C %ClientLocation%\SkinTemp\Temp
        cd %ClientLocation%\SkinTemp\Temp\
        xcopy %ClientLocation%\SkinTemp\Temp\%localloadbackup%\vehicles\ \%ClientLocation%\res_mods\%ClientVersion%\ /e
)
    goto Install