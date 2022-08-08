「SyncTank」
=======================

# what is「SyncTank」?
SyncTank is World Of Tank automatic Skin Downloader

## For anyone who want to use this tool

1. You have to edit code.
Client side - First Start, Program will make some files on c:\SyncTank. edit "DLserver.inf" (e.g : mashiroDL.i234.me)
Server side - must have some files. 
```(root)─WoTskin─PySkin┬Skinlist.inf

                     ├```
---

2. SyncTankZipMaker is for user who want to make server, Drag and Drop your skin on SkinFileMake - DragAndDrop.bat and you can get zip file ex)G89_Leopard1 -> G89.zip
---

3. Server need several file. 

{main}\WoTskin\Skin\{Skins, ex)G73.zip}

{main}\WoTskin\Skinlist.inf

{main}\WoTskin\Version.inf


Skinlist.inf is literally List of server skin file on {main}\WoTskin\Skin\ 

ex)

GB81_FV4004
G73_E50_Ausf_M
G89_Leopard1
G97_Waffentrager_IV
G121_Grille_15_L63
It17_Progetto_CC55_mod_54


Version.inf is WoT client res_mods version ex)1.16.1.0


-----
SkinFileMake


make config file in c:\SyncTank

1. 잘못된 입력시 (예 : fuck) rollback - Half sucess(When u type Country code(ex : F,It), rollback is not work)
2. 파일 네이티브 인스톨 -> 평소 인스톨 절차 순서 변경을 통해 그냥 설치하게 놔둠
3. 일괄 다운로드 메뉴 추가
4. 병렬처리 -> 