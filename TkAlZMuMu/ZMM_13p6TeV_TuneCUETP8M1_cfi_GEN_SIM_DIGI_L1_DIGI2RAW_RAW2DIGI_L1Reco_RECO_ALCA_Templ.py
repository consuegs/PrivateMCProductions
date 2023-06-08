# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: ZMM_13TeV_TuneCUETP8M1_cfi --conditions auto:phase1_2018_realistic -n 100 --era Run2_2018 --eventcontent ALCARECO -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO,ALCA:TkAlZMuMu --datatier ALCARECO --beamspot Realistic25ns13TeVEarly2018Collision --geometry DB:Extended
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

####################################################################
def customise_ZMMOnly(process):
	if hasattr(process,'ALCARECOStreamTkAlZMuMuOutPath'):
		process=customise_alcareco(process)
	return process   

####################################################################
def customise_alcareco(process):
	print "customising the alcareco"
	process.pathALCARECOTkAlZMuMu.remove(process.ALCARECOTkAlZMuMuHLT)
	return process

from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process('RECO',Run3)

###################################################################
# Setup 'standard' options
###################################################################
options = VarParsing.VarParsing()

options.register('myseed',
                 1,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "my seed for the job (1 is default)")

options.register('maxEvents',
		 5,
		 VarParsing.VarParsing.multiplicity.singleton,
		 VarParsing.VarParsing.varType.int,
		 "Number of events to process (-1 for all)")

options.register ('GlobalTag',
                  '126X_mcRun3_2022_realistic_postEE_v2',
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
		  "Global Tag to select")

options.parseArguments()

print "my seed is: ", options.myseed

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13p6TeVEarly2022Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreamsMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# configure seed
process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(options.myseed)
process.RandomNumberGeneratorService.generator.engineName = cms.untracked.string('TRandom3')

process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(options.myseed)
process.RandomNumberGeneratorService.VtxSmeared.engineName = cms.untracked.string('TRandom3') 

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

myFirstEvent = (options.maxEvents * options.myseed)+1
print "firs Event:",myFirstEvent

# Input source
process.source = cms.Source("EmptySource",
			    firstEvent = cms.untracked.uint32(myFirstEvent),
			    firstLuminosityBlock = cms.untracked.uint32(options.myseed+1)
			    )

#Setup FWK for multithreaded                                                                                                  

process.options = cms.untracked.PSet()                                                                              
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)


# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('ZMM_13p6TeV_TuneCUETP8M1_cfi nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,options.GlobalTag, '')

process.GlobalTag.toGet = cms.VPSet(
     cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
          tag = cms.string('BeamSpotObjects_Realistic25ns_13p6TeVCollisions_Early2022_v3_mc'),
          connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
          ),     
     )

# Output definition
outrootfile='file:step1_ZMM_13p6TeV_TuneCUETP8M1_'+str(process.GlobalTag.globaltag.value())+"_"+str(options.maxEvents)+'_evts_seed_'+str(options.myseed)+'.root'
print 'output file name:', outrootfile

# Additional output definition
process.ALCARECOStreamTkAlZMuMu = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMu')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlZMuMu')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string(outrootfile),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep *_ALCARECOTkAlZMuMu_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_offlinePrimaryVertices_*_*'
    )
)

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
process.mix.digitizers.pixel.ThresholdInElectrons_BPix_L1 = cms.double(1300.0)
process.mix.digitizers.pixel.ThresholdInElectrons_BPix_L2 = cms.double(1600.0)
process.mix.digitizers.pixel.ThresholdInElectrons_BPix = cms.double(1600.0)
process.mix.digitizers.pixel.ThresholdInElectrons_FPix = cms.double(1600)   
process.PixelCPEGenericESProducer.IrradiationBiasCorrection = True
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlZMuMu_noDrop.outputCommands)

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'WeakSingleBoson:ffbar2gmZ = on', 
            '23:onMode = off', 
            '23:onIfAny = 13', 
            'PhaseSpace:mHatMin = 75.'
        ),
        pythia8CUEP8M1Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13600.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinPt = cms.untracked.vdouble(2.5, 2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13),
    Status = cms.untracked.vint32(1, 1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.mumugenfilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamTkAlZMuMuOutPath = cms.EndPath(process.ALCARECOStreamTkAlZMuMu)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.pathALCARECOTkAlZMuMu,process.endjob_step,process.ALCARECOStreamTkAlZMuMuOutPath)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 




# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

##### hack to remove check on HLT
process = customise_ZMMOnly(process)
