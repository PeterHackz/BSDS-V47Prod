from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1656503707) # timespamp that was at the end before
        self.writeVInt(1995904808) # new timespamp
        self.writeVInt(2022180) # timestamp, Logic Daily Data begin
        self.writeVInt(72292) # timestamp
        self.writeVInt(9500) # current trophies
        self.writeVInt(9500) # highest trophies
        self.writeVInt(9500) # highest trophies today?
        self.writeVInt(100) # collected trophy road rewards
        self.writeVInt(120000) # exp points
        self.writeDataReference(28, 0) # profile icon
        self.writeDataReference(43, 0) # name color

        self.writeVInt(20) # played game mode count
        for x in range(20):
            self.writeVInt(x)

        self.writeVInt(0) # selected skin count

        self.writeVInt(0) # available ramdon skins

        self.writeVInt(0) # random skins

        self.writeVInt(630)
        for x in range(630):
            self.writeDataReference(29, x) # unlocked skin array

        self.writeVInt(0) # skin purchase option

        self.writeVInt(0) # unk skin array5

        self.writeVInt(0) # leaderboard region
        self.writeVInt(0) # highest trophies
        self.writeVInt(0) # tokens used in battle
        self.writeVInt(1) # control mode
        self.writeBoolean(True) # battle hints
        self.writeVInt(0) # token doubler left
        self.writeVInt(2232292) # trophy league timer
        self.writeVInt(482692) # power play timer
        self.writeVInt(421492) # Brawl pass season timer

        self.writeVInt(0) # 
        self.writeVInt(0) # 
        self.writeVInt(0) # drop chance of characters in boxes
        # self.writeVInt(93)
        # self.writeVInt(206)
        # self.writeVInt(456)
        # self.writeVInt(1001)
        # self.writeVInt(2264)

        self.writeByte(1) # false, false, true
        self.writeVInt(2) # token doubler  new tag state
        self.writeVInt(2) # event tickets new tag state
        self.writeVInt(2) # coins pack new tag state
        self.writeVInt(0) # name change cost
        self.writeVInt(0) # timer for next name change

        self.writeVInt(0) # shop offer count
        self.writeVInt(200) # tokens for battle
        self.writeVInt(-64) # timer for new token

        self.writeVInt(0) # count

        self.writeVInt(0) # unk
        self.writeVInt(0) # unk2
        self.writeVInt(1)
        self.writeDataReference(16, 65) # selected brawler
        self.writeString('CA') # location
        self.writeString()

        self.writeVInt(0) # count resourced gained

        self.writeVInt(0) # count 0

        self.writeVInt(16) # count Brawl Pass Season
        for season in range(16):

            self.writeVInt(season)
            self.writeVInt(500) # season tokens collected
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeByte(2) # Premium rewards claimed level
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeByte(1) # free rewards claimed level
            self.writeInt(1)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True) # quests
        self.writeVInt(0) # count of quests
        self.writeVInt(0)
        self.writeVInt(47278)

        self.writeBoolean(False) # Vanity items
        self.writeVInt(1) # Vanity Count
        self.writeVInt(0)
        self.writeVInt(0) # vanity item

        self.writeBoolean(False) # Power League season data
        self.writeInt(164) # Logic Daily Data end
        self.writeVInt(-15789) # Logic Conf Data begin

        self.writeVInt(32) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18)
        self.writeVInt(19)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        self.writeVInt(1) # event data count
        self.writeVInt(-1184283511)
        self.writeVInt(32)
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(5)
        self.writeDataReference(15, 122) # map id
        self.writeVInt(-64)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # map maker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array start
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # chronos text entry
        self.writeVInt(-64)
        self.writeByte(0)
        self.writeVInt(-64)

        self.writeVInt(0) #upcoming event count

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeVInt(0) #locked for chronos
        for x in range(0):
            self.writeDataReference(16, 61)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(1) # int entry count
        self.writeInt(1)
        self.writeInt(41000054) #theme

        self.writeVInt(0) #  Timed int entry count

        self.writeVInt(0) # custom event

        self.writeVInt(2) # new arrayvInt
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2) # new arrayvInt
        self.writeVInt(1)
        self.writeVInt(-64)
        self.writeVInt(2) # new arrayvInt
        self.writeVInt(1)
        self.writeVInt(4)

        self.writeVInt(0) #new count v46

        self.writeVInt(0) #new count v46

        self.writeLong(0, 1) # Player ID

        self.writeVInt(0) # Notification factory

        self.writeVInt(-64)
        self.writeBoolean(False)
        self.writeVInt(0) # Gatcha drop
        self.writeVInt(0) # End of LogicClientHome

        self.writeVInt(0)
        self.writeBoolean(False)

        self.writeVInt(0) # new function v46
        self.writeBoolean(False) #something weird, contains multiples if check
        

        # self.writeVInt(0) #end of LogicClientHome

        #Logic Client Avatar begin
        self.writeVLong(0, 1) # player id
        self.writeVLong(0, 1)
        self.writeVLong(0, 1)
        self.writeString('risporce') # Player Name
        self.writeBoolean(True) # name set
        self.writeString()

        self.writeVInt(17) # Commodity Count

        unlocked_brawler = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 95, 100, 105, 110, 115, 120, 125, 130, 177, 182, 188, 194, 200, 206, 218, 224, 230, 236, 279, 296, 303, 320, 327, 334, 341, 358, 365, 372, 379, 386, 393, 410, 417, 427, 434, 448, 466, 474, 491, 499, 507, 515, 523, 531, 539]
        self.writeVInt(len(unlocked_brawler) + 3) # unlocked brawlers + resources
        for x in unlocked_brawler:
            self.writeDataReference(23, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(1090)

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(73)

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(22)

        self.writeVInt(66) # HeroScore
        for x in range(66):
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(1250)
        
        self.writeVInt(66)
        for x in range(66):
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeVInt(0) # Array

        self.writeVInt(66) # HeroPower
        for x in range(66):
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(1)
        
        self.writeVInt(66) # HeroLevel
        for x in range(66):
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(10)

        self.writeVInt(0) # hero star power and gadget

        self.writeVInt(66) # HeroSeenState
        for x in range(66):
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(2)

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array

        self.writeVInt(999) # Diamonds
        self.writeVInt(999) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion