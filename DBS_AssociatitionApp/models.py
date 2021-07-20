from django.db import models

class Mdactorcategory(models.Model):
    actorcategoryid = models.IntegerField(db_column='actorCategoryID', primary_key=True)  # Field name made lowercase.
    actorcategoryname = models.CharField(db_column='actorCategoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdActorCategory'

class Mdassettypes(models.Model):
    assettypeid = models.IntegerField(db_column='assetTypeID', primary_key=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='assetType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentassettype = models.BigIntegerField(db_column='parentAssetType', blank=True, null=True)  # Field name made lowercase.
    effectivedepreciation = models.DecimalField(db_column='effectiveDepreciation', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdAssetTypes'


class Mdcastatus(models.Model):
    castatusid = models.IntegerField(db_column='caStatusID', primary_key=True)  # Field name made lowercase.
    castatusname = models.CharField(db_column='caStatusName', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdCAStatus'


class Mddimensions(models.Model):
    dimensionid = models.AutoField(db_column='dimensionID', primary_key=True)  # Field name made lowercase.
    mgtdimension = models.CharField(db_column='mgtDimension', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dimdescription = models.TextField(db_column='dimDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdDimensions'


class Mddrivertypes(models.Model):
    drivertypeid = models.AutoField(db_column='driverTypeID', primary_key=True)  # Field name made lowercase.
    drivertypename = models.CharField(db_column='driverTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentdrivertype = models.ForeignKey('self', models.DO_NOTHING, db_column='parentDriverType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdDriverTypes'


class Mdgeneralscale(models.Model):
    scaleid = models.AutoField(db_column='scaleID', primary_key=True)  # Field name made lowercase.
    qtyinticator = models.IntegerField(db_column='qtyInticator', blank=True)  # Field name made lowercase.
    qlyindicator = models.CharField(db_column='qlyIndicator', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdGeneralScale'


class Mdmanagementmethods(models.Model):
    managementmethodid = models.IntegerField(db_column='managementMethodID', primary_key=True)  # Field name made lowercase.
    managementmethodname = models.CharField(db_column='managementMethodName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=250, blank=True, null=True)
    parentmanagementmethod = models.ForeignKey('self', models.DO_NOTHING, db_column='parentManagementMethod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdManagementMethods'


class Mdoccurrences(models.Model):
    occurrenceid = models.IntegerField(db_column='occurrenceID', primary_key=True)  # Field name made lowercase.
    occurrencename = models.CharField(db_column='occurrenceName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdOccurrences'


class Mdorgtypes(models.Model):
    orgtypeid = models.IntegerField(db_column='orgTypeID', primary_key=True)  # Field name made lowercase.
    orgtypename = models.CharField(db_column='orgTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdOrgTypes'


class Mdphases(models.Model):
    phaseid = models.IntegerField(db_column='phaseID', primary_key=True)  # Field name made lowercase.
    phasename = models.CharField(db_column='phaseName', max_length=75, blank=True, null=True)  # Field name made lowercase.
    desctiption = models.CharField(max_length=250, blank=True, null=True)
    methodid = models.ForeignKey(Mdmanagementmethods, models.DO_NOTHING, db_column='methodID', blank=True, null=True)  # Field name made lowercase.
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mdPhases'


class Mdstakes(models.Model):
    stakeid = models.IntegerField(db_column='stakeID', primary_key=True)  # Field name made lowercase.
    stakename = models.CharField(db_column='stakeName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdStakes'


class Mdstatus(models.Model):
    statusid = models.IntegerField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    statusname = models.CharField(db_column='statusName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdStatus'


class Orgdrivers(models.Model):
    driverid = models.BigAutoField(db_column='driverID', primary_key=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='driverName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    driverdescription = models.TextField(db_column='driverDescription', blank=True, null=True)  # Field name made lowercase.
    parentdriver = models.BigIntegerField(db_column='parentDriver', blank=True, null=True)  # Field name made lowercase.
    plannedstart = models.DateField(db_column='plannedStart', blank=True, null=True)  # Field name made lowercase.
    plannedend = models.DateField(db_column='plannedEnd', blank=True, null=True)  # Field name made lowercase.
    actualstart = models.DateField(db_column='actualStart', blank=True, null=True)  # Field name made lowercase.
    actualend = models.DateField(db_column='actualEnd', blank=True, null=True)  # Field name made lowercase.
    cumulativeimportance = models.ForeignKey(Mdgeneralscale, models.DO_NOTHING, db_column='cumulativeImportance', blank=True, null=True)  # Field name made lowercase.
    drivertype = models.ForeignKey(Mddrivertypes, models.DO_NOTHING, db_column='driverType', blank=True, null=True)  # Field name made lowercase.
    approvedon = models.DateField(db_column='approvedOn', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateField(db_column='createdOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orgDrivers'

class Missions(models.Model):
    missionid = models.AutoField(db_column='missionID', primary_key=True)  # Field name made lowercase.
    statement = models.TextField(blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    priority = models.ForeignKey('Mdgeneralscale', models.DO_NOTHING, db_column='priority', blank=True, null=True)
    missiontitle = models.CharField(db_column='missionTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Missions'

class Contributionstasks(models.Model):
    contributionid = models.BigIntegerField(db_column='contributionID', primary_key=True)  # Field name made lowercase.
    contributionname = models.CharField(db_column='contributionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    starton = models.DateField(db_column='startOn', blank=True, null=True)  # Field name made lowercase.
    endon = models.DateField(db_column='endOn', blank=True, null=True)  # Field name made lowercase.
    occurrenceid = models.ForeignKey('Mdoccurrences', models.DO_NOTHING, db_column='occurrenceID', blank=True, null=True)  # Field name made lowercase.
    statusid = models.ForeignKey('Mdstatus', models.DO_NOTHING, db_column='statusID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributionsTasks'


class Dispensationrecords(models.Model):
    dispensationid = models.BigAutoField(db_column='dispensationID', primary_key=True)  # Field name made lowercase.
    dispensationuntil = models.DateField(db_column='dispensationUntil', blank=True, null=True)  # Field name made lowercase.
    dispensationreason = models.TextField(db_column='dispensationReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dispensationRecords'
class Orgdeliverables(models.Model):
    deliverableid = models.BigAutoField(db_column='deliverableID', primary_key=True)  # Field name made lowercase.
    deliverablename = models.CharField(db_column='deliverableName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deliverabledescription = models.TextField(db_column='deliverableDescription', blank=True, null=True)  # Field name made lowercase.
    parentdeliverable = models.ForeignKey('self', models.DO_NOTHING, db_column='parentDeliverable', blank=True, null=True)  # Field name made lowercase.
    deliverabletype = models.ForeignKey(Mdassettypes, models.DO_NOTHING, db_column='deliverableType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orgDeliverables'


class Orggoals(models.Model):
    goalid = models.BigAutoField(db_column='goalID', primary_key=True)  # Field name made lowercase.
    goalname = models.CharField(db_column='goalName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goaldescription = models.TextField(db_column='goalDescription', blank=True, null=True)  # Field name made lowercase.
    parentgoal = models.BigIntegerField(db_column='parentGoal', blank=True, null=True)  # Field name made lowercase.
    plannedfor = models.DateField(db_column='plannedFor', blank=True, null=True)  # Field name made lowercase.
    achievedon = models.DateField(db_column='achievedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orgGoals'


class Orgmilestones(models.Model):
    milestoneid = models.BigAutoField(db_column='milestoneID', primary_key=True)  # Field name made lowercase.
    milestonename = models.CharField(db_column='milestoneName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    milestonedescription = models.TextField(db_column='milestoneDescription', blank=True, null=True)  # Field name made lowercase.
    parentmilestone = models.ForeignKey('self', models.DO_NOTHING, db_column='parentMilestone', blank=True, null=True)  # Field name made lowercase.
    plannedfor = models.DateField(db_column='plannedFor', blank=True, null=True)  # Field name made lowercase.
    achievedon = models.DateField(db_column='achievedOn', blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='sequenceNumber', blank=True, null=True)  # Field name made lowercase.
    completionpercentage = models.DecimalField(db_column='completionPercentage', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orgMilestones'

class Assodimimp(models.Model):
    dimensionid = models.IntegerField(db_column='dimensionID', primary_key=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Orgdrivers', models.DO_NOTHING, db_column='DriverID', blank=True, null=True)  # Field name made lowercase.
    importance = models.ForeignKey('Mdgeneralscale', models.DO_NOTHING, db_column='importance', blank=True, null=True)
    contributionscale = models.DecimalField(db_column='contributionScale', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assoDimImp'

class Assodso(models.Model):
    dsoid = models.BigIntegerField(db_column='dsoID', primary_key=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Orgdrivers', models.DO_NOTHING, db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    milestoneid = models.ForeignKey('Orgmilestones', models.DO_NOTHING, db_column='milestoneID', blank=True, null=True)  # Field name made lowercase.
    deliverableid = models.ForeignKey('Orgdeliverables', models.DO_NOTHING, db_column='deliverableID', blank=True, null=True)  # Field name made lowercase.
    goalid = models.ForeignKey('Orggoals', models.DO_NOTHING, db_column='goalID', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    priority = models.ForeignKey('Mdgeneralscale', models.DO_NOTHING, db_column='priority', blank=True, null=True)
    fulfillmentpercentage = models.DecimalField(db_column='fulfillmentPercentage', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assoDSO'

class Assomilestonesdispen(models.Model):
    milestoneid = models.ForeignKey('Orgmilestones', models.DO_NOTHING, db_column='milestoneID', blank=True, null=True)  # Field name made lowercase.
    dispensationid = models.ForeignKey('Dispensationrecords', models.DO_NOTHING, db_column='dispensationID', blank=True, null=True)  # Field name made lowercase.
    deliverableid = models.ForeignKey('Orgdeliverables', models.DO_NOTHING, db_column='deliverableID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assomilestonesDispen'

class Assomissiondrivers(models.Model):
    missionid = models.ForeignKey(Missions, models.DO_NOTHING, db_column='missionID', blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Orgdrivers', models.DO_NOTHING, db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    contributionscale = models.DecimalField(db_column='contributionScale', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assoMissionDrivers'

class Assostakeholderdso(models.Model):
    dsoid = models.ForeignKey(Assodso, models.DO_NOTHING, db_column='dsoID', blank=True, null=True)  # Field name made lowercase.
    isresponsible = models.BooleanField(db_column='IsResponsible', blank=True, null=True)  # Field name made lowercase.
    isaccountable = models.BooleanField(db_column='IsAccountable', blank=True, null=True)  # Field name made lowercase.
    isinformed = models.BooleanField(db_column='IsInformed', blank=True, null=True)  # Field name made lowercase.
    isconsulted = models.BooleanField(db_column='IsConsulted', blank=True, null=True)  # Field name made lowercase.
    staketype = models.ForeignKey('Mdstakes', models.DO_NOTHING, db_column='stakeType', blank=True, null=True)  # Field name made lowercase.
    contributionpercentage = models.DecimalField(db_column='contributionPercentage', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    contributionimportance = models.ForeignKey('Mdgeneralscale', models.DO_NOTHING, db_column='contributionImportance', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    stakeholderid = models.UUIDField(db_column='stakeholderID', blank=True, null=True)  # Field name made lowercase.
    stakeholderfullname = models.CharField(db_column='stakeholderFullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stakeholderdirectoratedept = models.CharField(db_column='stakeholderDirectorateDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stakeholderroledesignation = models.CharField(db_column='stakeholderRoleDesignation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stakeholderdsoid = models.BigIntegerField(db_column='stakeholderDSOID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assoStakeholderDSO'


class Assostakeholderdsocontribution(models.Model):
    stakeholderdsoid = models.OneToOneField(Assostakeholderdso, models.DO_NOTHING, db_column='stakeholderDSOID', primary_key=True)  # Field name made lowercase.
    contributionid = models.ForeignKey('Contributionstasks', models.DO_NOTHING, db_column='contributionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assoStakeholderDSOContribution'

