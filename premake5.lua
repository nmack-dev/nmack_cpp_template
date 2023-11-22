-- premake5.lua
workspace "MyCppProject"
    configurations { "Debug", "Release" }

    -- Set the default platform to x64 for Visual Studio
    if os.target() == "windows" then
        platforms { "x64" }
    end

project "MyCppProject"
    kind "StaticLib"
    language "C++"
    cppdialect "C++20"
    targetdir ("bin/%{prj.name}/%{cfg.buildcfg}")
    objdir ("obj/%{prj.name}/%{cfg.buildcfg}")

    files 
    { 
        "src/**.cpp", 
        "include/**.h" 
    }

    includedirs 
    { 
        "include", 
        "external/googletest/googletest/include" 
    }

project "MyCppProjectTests"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++20"
    targetdir ("bin/%{prj.name}/%{cfg.buildcfg}")
    objdir ("obj/%{prj.name}/%{cfg.buildcfg}")
    
    files 
    { 
        "tests/**.cpp" 
    }

    includedirs 
    { 
        "include", 
        "external/googletest/googletest/include" 
    }

    links 
    { 
        "MyCppProject", 
        "external/googletest/build/lib/%{cfg.buildcfg}/gtest.lib" 
    }

    filter "configurations:Debug"
        defines { "DEBUG" }
        symbols "On"

    filter "configurations:Release"
        defines { "RELEASE" }
        optimize "On"
