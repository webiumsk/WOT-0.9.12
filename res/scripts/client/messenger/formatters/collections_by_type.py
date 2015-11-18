# 2015.11.18 11:57:28 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/messenger/formatters/collections_by_type.py
from chat_shared import SYS_MESSAGE_TYPE as _SM_TYPE
from messenger.formatters import service_channel as _sc
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
SERVER_FORMATTERS = {_SM_TYPE.serverReboot.index(): _sc.ServerRebootFormatter(),
 _SM_TYPE.serverRebootCancelled.index(): _sc.ServerRebootCancelledFormatter(),
 _SM_TYPE.battleResults.index(): _sc.BattleResultsFormatter(),
 _SM_TYPE.goldReceived.index(): _sc.GoldReceivedFormatter(),
 _SM_TYPE.invoiceReceived.index(): _sc.InvoiceReceivedFormatter(),
 _SM_TYPE.adminTextMessage.index(): _sc.AdminMessageFormatter(),
 _SM_TYPE.accountTypeChanged.index(): _sc.AccountTypeChangedFormatter(),
 _SM_TYPE.giftReceived.index(): _sc.GiftReceivedFormatter(),
 _SM_TYPE.autoMaintenance.index(): _sc.AutoMaintenanceFormatter(),
 _SM_TYPE.waresSold.index(): _sc.WaresSoldFormatter(),
 _SM_TYPE.waresBought.index(): _sc.WaresBoughtFormatter(),
 _SM_TYPE.premiumBought.index(): _sc.PremiumBoughtFormatter(),
 _SM_TYPE.premiumExtended.index(): _sc.PremiumExtendedFormatter(),
 _SM_TYPE.premiumExpired.index(): _sc.PremiumExpiredFormatter(),
 _SM_TYPE.prbArenaFinish.index(): _sc.PrebattleArenaFinishFormatter(),
 _SM_TYPE.prbKick.index(): _sc.PrebattleKickFormatter(),
 _SM_TYPE.prbDestruction.index(): _sc.PrebattleDestructionFormatter(),
 _SM_TYPE.vehicleCamouflageTimedOut.index(): _sc.VehCamouflageTimedOutFormatter(),
 _SM_TYPE.vehiclePlayerEmblemTimedOut.index(): _sc.VehEmblemTimedOutFormatter(),
 _SM_TYPE.vehiclePlayerInscriptionTimedOut.index(): _sc.VehInscriptionTimedOutFormatter(),
 _SM_TYPE.vehTypeLockExpired.index(): _sc.VehicleTypeLockExpired(),
 _SM_TYPE.serverDowntimeCompensation.index(): _sc.ServerDowntimeCompensation(),
 _SM_TYPE.achievementReceived.index(): _sc.AchievementFormatter(),
 _SM_TYPE.converter.index(): _sc.ConverterFormatter(),
 _SM_TYPE.tokenQuests.index(): _sc.TokenQuestsFormatter(),
 _SM_TYPE.notificationsCenter.index(): _sc.NCMessageFormatter(),
 _SM_TYPE.clanEvent.index(): _sc.ClanMessageFormatter(),
 _SM_TYPE.fortEvent.index(): _sc.FortMessageFormatter(),
 _SM_TYPE.fortBattleEnd.index(): _sc.FortBattleResultsFormatter(),
 _SM_TYPE.fortBattleRoundEnd.index(): _sc.FortBattleRoundEndFormatter(),
 _SM_TYPE.fortBattleInvite.index(): _sc.FortBattleInviteFormatter(),
 _SM_TYPE.vehicleRented.index(): _sc.VehicleRentedFormatter(),
 _SM_TYPE.rentalsExpired.index(): _sc.RentalsExpiredFormatter(),
 _SM_TYPE.refSystemQuests.index(): _sc.RefSystemQuestsFormatter(),
 _SM_TYPE.refSystemReferralBoughtVehicle.index(): _sc.RefSystemReferralBoughtVehicleFormatter(),
 _SM_TYPE.refSystemReferralContributedXP.index(): _sc.RefSystemReferralContributedXPFormatter(),
 _SM_TYPE.potapovQuestBonus.index(): _sc.PotapovQuestsFormatter(),
 _SM_TYPE.goodieRemoved.index(): _sc.GoodieRemovedFormatter()}
CLIENT_FORMATTERS = {SCH_CLIENT_MSG_TYPE.SYS_MSG_TYPE: _sc.ClientSysMessageFormatter(),
 SCH_CLIENT_MSG_TYPE.PREMIUM_ACCOUNT_EXPIRY_MSG: _sc.PremiumAccountExpiryFormatter(),
 SCH_CLIENT_MSG_TYPE.AOGAS_NOTIFY_TYPE: _sc.AOGASNotifyFormatter(),
 SCH_CLIENT_MSG_TYPE.ACTION_NOTIFY_TYPE: _sc.ActionNotificationFormatter(),
 SCH_CLIENT_MSG_TYPE.BATTLE_TUTORIAL_RESULTS_TYPE: _sc.BattleTutorialResultsFormatter()}
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\formatters\collections_by_type.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:57:28 St�edn� Evropa (b�n� �as)
