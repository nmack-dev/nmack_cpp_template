workspace "MyProject"
    configurations {"Debug", "Release"}
    platforms { "x64" }
    
    -- C++ as target language
    language "C++"
    targetdir "bin/%{cfg.buildcfg}"
    
    cppdialect "C++20"

    filter "configurations:Debug"
        -- Add the preprocessor definition DEBUG to debug builds
        defines { "DEBUG" }
        -- Ensure symbols are bundled with debug builds
        symbols "On"

    filter "configurations:Release"
        -- Add the preprocessor definition RELEASE to debug builds
        defines { "RELEASE" }
        -- Turn on compiler optimizations for release builds
        optimize "On"
    
    -- Static library config
    project "MyProject"
        kind "StaticLib"
        -- recursively glob .h and .cpp files in the lib directory
        files { "include/**.h", "src/**.cpp" }
        includedirs { "include" }

    project "GoogleTest"
        kind "StaticLib"
        files { "external/googletest/googletest/src/gtest-all.cc" }
        includedirs { "external/googletest/googletest/include", "external/googletest/googletest" }
    
    -- Runtime config
    project "MyProjectTest"
        kind "ConsoleApp"
        -- recursively glob .h and .cpp files in the runtime directory
        files { "tests/**.h", "tests/**.cpp" }
        -- link the RePlexLib library at runtime
        includedirs { "include", "external/googletest/googletest/include" }
        links { "GoogleTest" }
